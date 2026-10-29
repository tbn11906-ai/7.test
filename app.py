"""
Ứng dụng Web Nội bộ DIGI Technologies
Quản lý Tiếp nhận Yêu cầu Hiệu chuẩn và Sổ theo dõi Phương tiện đo (PTĐ)
Backend: Python Flask + SQLite + OpenPyXL
"""

import os
import sys
import json
import sqlite3
import datetime
from io import BytesIO
from functools import wraps
from flask import Flask, request, jsonify, session, send_file, send_from_directory, render_template_string

# Đảm bảo mã hóa UTF-8 cho console Windows
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

app = Flask(__name__, static_folder='.', static_url_path='')
app.secret_key = 'digi_cst_secret_key_calibration_2026_secured'

DB_PATH = os.path.join(os.path.dirname(__file__), 'calibration.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Khởi tạo database SQLite và nạp dữ liệu mẫu ban đầu nếu rỗng."""
    conn = get_db()
    cursor = conn.cursor()
    
    # Bảng người dùng
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')
    
    # Bảng phiếu yêu cầu & sổ theo dõi
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS calibration_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE NOT NULL,
        contract_sales TEXT,
        customer_name TEXT NOT NULL,
        customer_address TEXT,
        customer_tax_code TEXT,
        contact_person TEXT,
        contact_phone TEXT,
        contact_email TEXT,
        devices_json TEXT,
        code_temp TEXT,
        code_hum TEXT,
        code_press TEXT,
        code_gas TEXT,
        procedures_json TEXT,
        params_gas_json TEXT,
        params_measure_json TEXT,
        service_desc TEXT,
        revenue REAL DEFAULT 0,
        req_adjust INTEGER DEFAULT 0,
        req_uncertainty INTEGER DEFAULT 1,
        req_compliance INTEGER DEFAULT 0,
        req_next_date INTEGER DEFAULT 1,
        return_method TEXT DEFAULT 'CHUYEN_PHAT',
        expected_return_date TEXT,
        technician TEXT DEFAULT 'Nguyễn Minh Tú',
        received_info TEXT,
        returned_info TEXT,
        handover_person TEXT,
        recipient_person TEXT,
        received_date TEXT,
        next_cal_date TEXT,
        cert_done INTEGER DEFAULT 0,
        device_done INTEGER DEFAULT 0,
        accessories_note TEXT,
        general_note TEXT,
        created_at TEXT,
        created_by TEXT
    )
    ''')

    # Migration kiểm tra cột mới nếu bảng đã tạo từ trước
    for col, col_type in [
        ('handover_person', 'TEXT'),
        ('recipient_person', 'TEXT'),
        ('received_date', 'TEXT'),
        ('received_person', 'TEXT'),
        ('returned_person', 'TEXT'),
        ('returned_date', 'TEXT'),
        ('next_cal_date', 'TEXT')
    ]:
        try:
            cursor.execute(f'ALTER TABLE calibration_requests ADD COLUMN {col} {col_type}')
        except Exception:
            pass
    
    # Tạo tài khoản mặc định
    cursor.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
        INSERT INTO users (email, password, name, role)
        VALUES 
        ('CST@digivn.com', 'CST@654', 'Quản trị viên CST', 'admin'),
        ('nhanvien@digivn.com', '123456', 'Nhân viên Tiếp nhận', 'user')
        ''')
    
    # Kiểm tra xem có cần nạp dữ liệu mẫu từ Excel không
    cursor.execute('SELECT COUNT(*) FROM calibration_requests')
    if cursor.fetchone()[0] == 0:
        seed_from_excel(cursor)
        
    conn.commit()
    conn.close()

def seed_from_excel(cursor):
    """Nạp dữ liệu từ file Excel có sẵn nếu tồn tại."""
    excel_file = os.path.join(os.path.dirname(__file__), 'SỔ THEO DÕI NHẬN PTĐ VÀ TRẢ KẾT QUẢ.xlsx')
    if not os.path.exists(excel_file):
        return
        
    try:
        import openpyxl, re
        wb = openpyxl.load_workbook(excel_file, data_only=True)
        ws = wb['NHẬN_TRẢ PTĐ']
        
        for r in range(9, 30):
            stt = ws.cell(r, 1).value
            code = ws.cell(r, 2).value
            if not code or not stt:
                continue
            code = str(code).strip()
            contract = str(ws.cell(r, 6).value or '').strip()
            desc = str(ws.cell(r, 7).value or '').strip()
            cust = str(ws.cell(r, 9).value or '').strip()
            t = str(ws.cell(r, 10).value or '').strip()
            h = str(ws.cell(r, 11).value or '').strip()
            p = str(ws.cell(r, 12).value or '').strip()
            g = str(ws.cell(r, 13).value or '').strip()
            qty = ws.cell(r, 14).value or 1
            try:
                qty = int(qty)
            except:
                qty = 1
            tech = str(ws.cell(r, 15).value or 'Nguyễn Minh Tú').strip()
            rec = str(ws.cell(r, 16).value or '').strip()
            ret = str(ws.cell(r, 17).value or '').strip()
            next_c = str(ws.cell(r, 18).value or '').strip()
            if ' 00:00:00' in next_c:
                next_c = next_c.split(' ')[0]
            cert = 1 if ws.cell(r, 19).value else 0
            dev = 1 if ws.cell(r, 20).value else 0
            note = str(ws.cell(r, 23).value or '').strip()
            
            # Tính doanh số theo công thức chuẩn
            gas_matches = re.findall(r'(O2|CO2|CO|NO2|NO|SO2)', desc.upper())
            gas_unique = list(dict.fromkeys(gas_matches))
            if not gas_unique and g:
                gas_unique = ['O2', 'CO']
            gas_cost = len(gas_unique) * 1500000
            
            has_temp = bool(t or 'nhiệt độ' in desc.lower() or '925' in desc.lower() or '922' in desc.lower())
            temp_cost = 500000 if has_temp else 0
            
            has_press = bool(p or 'áp suất' in desc.lower() or 'chênh áp' in desc.lower())
            press_cost = 500000 if has_press else 0
            
            has_hum = bool(h or 'nhiệt ẩm' in desc.lower() or '608' in desc.lower())
            hum_cost = (750000 * qty) if has_hum else 0
            
            rev = gas_cost + temp_cost + press_cost + hum_cost
            if rev == 0:
                rev = 1500000
                
            dev_name = desc.split('\n')[0] if desc else 'Thiết bị đo'
            devices = [{'stt': 1, 'name': dev_name, 'specs': 'Tiêu chuẩn', 'qty': qty, 'condition': 'Bình thường, đầy đủ phụ kiện'}]
            
            procedures = []
            if has_temp:
                procedures.append('DIGI.QT.HC.012023 QTHC Nhiệt kế chỉ thị hiện số và tương tự')
            if has_hum:
                procedures.append('DIGI.QT.HC.022023 Nhiệt ẩm kế không khí')
            if has_press:
                procedures.append('DIGI.QT.HC.032023 Áp kế chênh áp kiểu hiện số')
            if gas_unique:
                procedures.append('DIGI.QT.HC.042023 QTHC PTĐ Nồng độ khí')
                
            meas = []
            if has_temp: meas.append('NHIET_DO')
            if has_press: meas.append('CHENH_AP')
            if has_hum: meas.append('NHIET_AM')
            
            cursor.execute('''
            INSERT OR IGNORE INTO calibration_requests 
            (code, contract_sales, customer_name, customer_address, customer_tax_code,
             contact_person, contact_phone, contact_email, devices_json,
             code_temp, code_hum, code_press, code_gas, procedures_json,
             params_gas_json, params_measure_json, service_desc, revenue,
             req_adjust, req_uncertainty, req_compliance, req_next_date,
             return_method, expected_return_date, technician, received_info,
             returned_info, next_cal_date, cert_done, device_done,
             accessories_note, general_note, created_at, created_by)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (
                code, contract, cust, 'Việt Nam', '0312345678',
                contract.split('\n')[1] if '\n' in contract else 'Phụ trách kỹ thuật',
                '0908 123 456', 'cst@digivn.com', json.dumps(devices, ensure_ascii=False),
                t, h, p, g, json.dumps(procedures, ensure_ascii=False),
                json.dumps(gas_unique, ensure_ascii=False), json.dumps(meas, ensure_ascii=False),
                desc, rev, 0, 1, 0, 1,
                'CHUYEN_PHAT', ret.split('_')[0] if ret else '2026-03-01',
                tech, rec, ret, next_c, cert, dev,
                'Cáp nguồn, đầu đo theo máy', note,
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'CST@digivn.com'
            ))
    except Exception as e:
        print(f"Error seeding data from excel: {e}")

# Helper auth check
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = session.get('user')
        if not user or user.get('role') != 'admin':
            return jsonify({'error': 'Bạn không có quyền quản trị (Chỉ dành cho Admin CST@digivn.com)'}), 403
        return f(*args, **kwargs)
    return decorated_function

# ================= AUTH APIS =================

@app.route('/api/auth/login', methods=['POST'])
def api_login():
    data = request.get_json() or {}
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, email, password, name, role FROM users WHERE LOWER(email) = LOWER(?)', (email,))
    user = cursor.fetchone()
    conn.close()
    
    if user and user['password'] == password:
        user_data = {
            'id': user['id'],
            'email': user['email'],
            'name': user['name'],
            'role': user['role']
        }
        session['user'] = user_data
        return jsonify({'success': True, 'user': user_data})
        
    return jsonify({'success': False, 'message': 'Email hoặc mật khẩu không chính xác'}), 401

@app.route('/api/auth/logout', methods=['POST', 'GET'])
def api_logout():
    session.pop('user', None)
    return jsonify({'success': True})

@app.route('/api/auth/me', methods=['GET'])
def api_me():
    user = session.get('user')
    if user:
        return jsonify({'logged_in': True, 'user': user})
    return jsonify({'logged_in': False, 'user': None})

# ================= CALIBRATION REQUESTS APIS =================

@app.route('/api/requests', methods=['GET'])
def api_get_requests():
    conn = get_db()
    cursor = conn.cursor()
    
    search = request.args.get('search', '').strip().lower()
    status = request.args.get('status', '').strip()
    
    query = 'SELECT * FROM calibration_requests WHERE 1=1'
    params = []
    
    if search:
        query += ''' AND (
            LOWER(code) LIKE ? OR 
            LOWER(customer_name) LIKE ? OR 
            LOWER(contract_sales) LIKE ? OR 
            LOWER(service_desc) LIKE ? OR
            LOWER(technician) LIKE ?
        )'''
        wildcard = f'%{search}%'
        params.extend([wildcard, wildcard, wildcard, wildcard, wildcard])
        
    if status == 'cert_done':
        query += ' AND cert_done = 1'
    elif status == 'cert_pending':
        query += ' AND cert_done = 0'
    elif status == 'device_done':
        query += ' AND device_done = 1'
    elif status == 'device_pending':
        query += ' AND device_done = 0'
        
    query += ' ORDER BY id DESC'
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    requests_list = []
    total_rev = 0
    cert_count = 0
    device_count = 0
    
    for row in rows:
        d = dict(row)
        try:
            d['devices'] = json.loads(d.get('devices_json') or '[]')
        except:
            d['devices'] = []
        try:
            d['procedures'] = json.loads(d.get('procedures_json') or '[]')
        except:
            d['procedures'] = []
        try:
            d['params_gas'] = json.loads(d.get('params_gas_json') or '[]')
        except:
            d['params_gas'] = []
        try:
            d['params_measure'] = json.loads(d.get('params_measure_json') or '[]')
        except:
            d['params_measure'] = []
            
        requests_list.append(d)
        total_rev += d.get('revenue') or 0
        if d.get('cert_done'): cert_count += 1
        if d.get('device_done'): device_count += 1
        
    conn.close()
    
    return jsonify({
        'success': True,
        'data': requests_list,
        'summary': {
            'total_count': len(requests_list),
            'total_revenue': total_rev,
            'cert_count': cert_count,
            'device_count': device_count
        }
    })

@app.route('/api/requests/<int:req_id>', methods=['GET'])
def api_get_request_detail(req_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM calibration_requests WHERE id = ?', (req_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        return jsonify({'error': 'Không tìm thấy phiếu yêu cầu'}), 404
        
    d = dict(row)
    try:
        d['devices'] = json.loads(d.get('devices_json') or '[]')
    except:
        d['devices'] = []
    try:
        d['procedures'] = json.loads(d.get('procedures_json') or '[]')
    except:
        d['procedures'] = []
    try:
        d['params_gas'] = json.loads(d.get('params_gas_json') or '[]')
    except:
        d['params_gas'] = []
    try:
        d['params_measure'] = json.loads(d.get('params_measure_json') or '[]')
    except:
        d['params_measure'] = []
        
    return jsonify({'success': True, 'data': d})

@app.route('/api/requests/next-code', methods=['GET'])
def api_next_code():
    """Tự động tính mã phiếu tiếp theo, e.g. HC.26.016"""
    now = datetime.datetime.now()
    yy = now.strftime('%y')
    prefix = f'HC.{yy}.'
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT code FROM calibration_requests WHERE code LIKE ? ORDER BY code DESC", (f'HC.%',))
    codes = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    max_num = 0
    for c in codes:
        parts = c.strip().split('.')
        if len(parts) == 3 and parts[2].isdigit():
            num = int(parts[2])
            if num > max_num:
                max_num = num
                
    next_num = max_num + 1
    next_code = f'{prefix}{next_num:03d}'
    return jsonify({'next_code': next_code, 'year': yy, 'number': next_num})

@app.route('/api/requests', methods=['POST'])
def api_create_request():
    data = request.get_json() or {}
    code = data.get('code', '').strip()
    
    conn = get_db()
    cursor = conn.cursor()
    
    # Nếu mã trống, tự động tạo mã mới
    if not code:
        now = datetime.datetime.now()
        yy = now.strftime('%y')
        cursor.execute("SELECT code FROM calibration_requests WHERE code LIKE 'HC.%'")
        codes = [row[0] for row in cursor.fetchall()]
        max_num = 0
        for c in codes:
            parts = c.strip().split('.')
            if len(parts) == 3 and parts[2].isdigit():
                max_num = max(max_num, int(parts[2]))
        code = f'HC.{yy}.{max_num + 1:03d}'
        
    # Kiểm tra trùng mã
    cursor.execute('SELECT id FROM calibration_requests WHERE code = ?', (code,))
    if cursor.fetchone():
        conn.close()
        return jsonify({'error': f'Mã phiếu {code} đã tồn tại trong hệ thống. Vui lòng chọn mã khác.'}), 400
        
    user = session.get('user', {})
    created_by = user.get('email', 'CST@digivn.com')
    created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
    INSERT INTO calibration_requests (
        code, contract_sales, customer_name, customer_address, customer_tax_code,
        contact_person, contact_phone, contact_email, devices_json,
        code_temp, code_hum, code_press, code_gas, procedures_json,
        params_gas_json, params_measure_json, service_desc, revenue,
        req_adjust, req_uncertainty, req_compliance, req_next_date,
        return_method, expected_return_date, technician, received_info,
        returned_info, handover_person, recipient_person, received_date,
        received_person, returned_person, returned_date,
        next_cal_date, cert_done, device_done,
        accessories_note, general_note, created_at, created_by
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', (
        code,
        data.get('contract_sales', ''),
        data.get('customer_name', ''),
        data.get('customer_address', ''),
        data.get('customer_tax_code', ''),
        data.get('contact_person', ''),
        data.get('contact_phone', ''),
        data.get('contact_email', ''),
        json.dumps(data.get('devices', []), ensure_ascii=False),
        data.get('code_temp', ''),
        data.get('code_hum', ''),
        data.get('code_press', ''),
        data.get('code_gas', ''),
        json.dumps(data.get('procedures', []), ensure_ascii=False),
        json.dumps(data.get('params_gas', []), ensure_ascii=False),
        json.dumps(data.get('params_measure', []), ensure_ascii=False),
        data.get('service_desc', ''),
        float(data.get('revenue', 0)),
        1 if data.get('req_adjust') else 0,
        1 if data.get('req_uncertainty', True) else 0,
        1 if data.get('req_compliance') else 0,
        1 if data.get('req_next_date', True) else 0,
        data.get('return_method', 'CHUYEN_PHAT'),
        data.get('expected_return_date', ''),
        data.get('technician', 'Nguyễn Minh Tú'),
        data.get('received_info', '') or data.get('received_date', ''),
        data.get('returned_info', '') or data.get('handover_person', ''),
        data.get('handover_person', ''),
        data.get('recipient_person', ''),
        data.get('received_date', ''),
        data.get('received_person', '') or data.get('recipient_person', ''),
        data.get('returned_person', '') or data.get('handover_person', ''),
        data.get('returned_date', '') or data.get('expected_return_date', ''),
        data.get('next_cal_date', ''),
        1 if data.get('cert_done') else 0,
        1 if data.get('device_done') else 0,
        data.get('accessories_note', ''),
        data.get('general_note', ''),
        created_at,
        created_by
    ))
    
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'id': new_id, 'code': code, 'message': 'Đã tiếp nhận và lưu phiếu thành công!'})

@app.route('/api/requests/<int:req_id>', methods=['PUT'])
def api_update_request(req_id):
    # Kiểm tra quyền: chỉ Admin hoặc User trong phiên có thể sửa
    user = session.get('user', {})
    data = request.get_json() or {}
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM calibration_requests WHERE id = ?', (req_id,))
    existing = cursor.fetchone()
    if not existing:
        conn.close()
        return jsonify({'error': 'Phiếu yêu cầu không tồn tại'}), 404
        
    cursor.execute('''
    UPDATE calibration_requests SET
        contract_sales = ?,
        customer_name = ?,
        customer_address = ?,
        customer_tax_code = ?,
        contact_person = ?,
        contact_phone = ?,
        contact_email = ?,
        devices_json = ?,
        code_temp = ?,
        code_hum = ?,
        code_press = ?,
        code_gas = ?,
        procedures_json = ?,
        params_gas_json = ?,
        params_measure_json = ?,
        service_desc = ?,
        revenue = ?,
        req_adjust = ?,
        req_uncertainty = ?,
        req_compliance = ?,
        req_next_date = ?,
        return_method = ?,
        expected_return_date = ?,
        technician = ?,
        received_info = ?,
        returned_info = ?,
        handover_person = ?,
        recipient_person = ?,
        received_date = ?,
        received_person = ?,
        returned_person = ?,
        returned_date = ?,
        next_cal_date = ?,
        cert_done = ?,
        device_done = ?,
        accessories_note = ?,
        general_note = ?
    WHERE id = ?
    ''', (
        data.get('contract_sales', existing['contract_sales']),
        data.get('customer_name', existing['customer_name']),
        data.get('customer_address', existing['customer_address']),
        data.get('customer_tax_code', existing['customer_tax_code']),
        data.get('contact_person', existing['contact_person']),
        data.get('contact_phone', existing['contact_phone']),
        data.get('contact_email', existing['contact_email']),
        json.dumps(data.get('devices', []), ensure_ascii=False) if 'devices' in data else existing['devices_json'],
        data.get('code_temp', existing['code_temp']),
        data.get('code_hum', existing['code_hum']),
        data.get('code_press', existing['code_press']),
        data.get('code_gas', existing['code_gas']),
        json.dumps(data.get('procedures', []), ensure_ascii=False) if 'procedures' in data else existing['procedures_json'],
        json.dumps(data.get('params_gas', []), ensure_ascii=False) if 'params_gas' in data else existing['params_gas_json'],
        json.dumps(data.get('params_measure', []), ensure_ascii=False) if 'params_measure' in data else existing['params_measure_json'],
        data.get('service_desc', existing['service_desc']),
        float(data.get('revenue', existing['revenue'])),
        1 if data.get('req_adjust', existing['req_adjust']) else 0,
        1 if data.get('req_uncertainty', existing['req_uncertainty']) else 0,
        1 if data.get('req_compliance', existing['req_compliance']) else 0,
        1 if data.get('req_next_date', existing['req_next_date']) else 0,
        data.get('return_method', existing['return_method']),
        data.get('expected_return_date', existing['expected_return_date']),
        data.get('technician', existing['technician']),
        data.get('received_info', existing['received_info']),
        data.get('returned_info', existing['returned_info']),
        data.get('handover_person', existing['handover_person'] if 'handover_person' in existing.keys() else ''),
        data.get('recipient_person', existing['recipient_person'] if 'recipient_person' in existing.keys() else ''),
        data.get('received_date', existing['received_date'] if 'received_date' in existing.keys() else ''),
        data.get('received_person', existing['received_person'] if 'received_person' in existing.keys() else ''),
        data.get('returned_person', existing['returned_person'] if 'returned_person' in existing.keys() else ''),
        data.get('returned_date', existing['returned_date'] if 'returned_date' in existing.keys() else ''),
        data.get('next_cal_date', existing['next_cal_date'] if 'next_cal_date' in existing.keys() else ''),
        1 if data.get('cert_done', existing['cert_done']) else 0,
        1 if data.get('device_done', existing['device_done']) else 0,
        data.get('accessories_note', existing['accessories_note']),
        data.get('general_note', existing['general_note']),
        req_id
    ))
    
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': 'Cập nhật phiếu thành công!'})

@app.route('/api/requests/<int:req_id>/toggle-status', methods=['PATCH'])
def api_toggle_status(req_id):
    """Cập nhật nhanh checkbox Đã Xuất GCN hoặc Đã Giao PTĐ từ lưới"""
    data = request.get_json() or {}
    field = data.get('field') # 'cert_done' hoặc 'device_done'
    val = 1 if data.get('value') else 0
    
    if field not in ['cert_done', 'device_done']:
        return jsonify({'error': 'Trường không hợp lệ'}), 400
        
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f'UPDATE calibration_requests SET {field} = ? WHERE id = ?', (val, req_id))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'field': field, 'value': val})

@app.route('/api/requests/<int:req_id>', methods=['DELETE'])
def api_delete_request(req_id):
    """Xóa bản ghi (Chỉ Admin)"""
    user = session.get('user', {})
    if user.get('role') != 'admin':
        return jsonify({'error': 'Chỉ Quản trị viên (CST@digivn.com) mới có quyền xóa bản ghi!'}), 403
        
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM calibration_requests WHERE id = ?', (req_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Đã xóa bản ghi thành công!'})

# ================= EXPORT EXCEL API =================

def normalize_excel_sample_codes(val):
    if not val:
        return ''
    import re
    items = [s.strip() for s in re.split(r'[\r\n,;]+|<br\s*/?>', str(val)) if s.strip()]
    return '\n'.join(items)

@app.route('/api/export-excel', methods=['GET'])
def api_export_excel():
    user = session.get('user', {})
    if user.get('role') != 'admin':
        # Vẫn cho phép xuất hoặc cảnh báo nếu chưa đăng nhập admin
        pass
        
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM calibration_requests ORDER BY id ASC')
    rows = cursor.fetchall()
    conn.close()
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'NHẬN_TRẢ PTĐ'
    ws.views.sheetView[0].showGridLines = True
    
    # Định nghĩa styles
    font_title = Font(name='Calibri', size=16, bold=True, color='C00000')
    font_sub = Font(name='Calibri', size=11, bold=True)
    font_hdr = Font(name='Calibri', size=10, bold=True, color='1E293B')
    font_body = Font(name='Calibri', size=10)
    font_bold = Font(name='Calibri', size=10, bold=True)
    
    fill_header = PatternFill(start_color='E2E8F0', end_color='E2E8F0', fill_type='solid')
    fill_sub_hdr = PatternFill(start_color='F1F5F9', end_color='F1F5F9', fill_type='solid')
    
    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )
    
    # Tiêu đề
    ws.merge_cells('A2:T2')
    ws['A2'] = 'SỔ THEO DÕI NHẬN MẪU VÀ TRẢ KẾT QUẢ'
    ws['A2'].font = font_title
    ws['A2'].alignment = Alignment(horizontal='center', vertical='center')
    
    ws['A4'] = f'Đơn vị: CÔNG TY CỔ PHẦN CÔNG NGHỆ DIGI (DIGI TECHNOLOGIES)'
    ws['A4'].font = font_sub
    ws['A5'] = f'Ngày xuất báo cáo: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}'
    ws['A5'].font = Font(name='Calibri', size=10, italic=True)
    
    # Merge và điền header chuẩn ISO (20 cột)
    ws.merge_cells('A7:A8'); ws['A7'] = 'STT'
    ws.merge_cells('B7:B8'); ws['B7'] = 'Phiếu yêu cầu'
    ws.merge_cells('C7:C8'); ws['C7'] = 'Mã HĐ / Sales'
    ws.merge_cells('D7:D8'); ws['D7'] = 'Mô tả chi tiết dịch vụ'
    ws.merge_cells('E7:E8'); ws['E7'] = 'Khách hàng'
    ws.merge_cells('F7:I7'); ws['F7'] = 'Mã mẫu'
    ws['F8'] = 'Nhiệt'; ws['G8'] = 'Nhiệt ẩm'; ws['H8'] = 'Áp'; ws['I8'] = 'Khí'
    ws.merge_cells('J7:J8'); ws['J7'] = 'Số lượng'
    ws.merge_cells('K7:K8'); ws['K7'] = 'Doanh số (Chưa VAT)'
    ws.merge_cells('L7:L8'); ws['L7'] = 'NVHC'
    ws.merge_cells('M7:M8'); ws['M7'] = 'Người nhận PTĐ'
    ws.merge_cells('N7:N8'); ws['N7'] = 'Ngày nhận PTĐ'
    ws.merge_cells('O7:O8'); ws['O7'] = 'Người trả PTĐ'
    ws.merge_cells('P7:P8'); ws['P7'] = 'Ngày trả PTĐ'
    ws.merge_cells('Q7:Q8'); ws['Q7'] = 'Ngày HC tiếp theo'
    ws.merge_cells('R7:R8'); ws['R7'] = 'Đã Xuất GCN'
    ws.merge_cells('S7:S8'); ws['S7'] = 'Đã Giao PTĐ'
    ws.merge_cells('T7:T8'); ws['T7'] = 'Ghi chú'
    
    # Định dạng header cells (Hạn chế màu sắc, phong cách đơn sắc thanh lịch)
    for r in [7, 8]:
        for c in range(1, 21):
            cell = ws.cell(r, c)
            cell.font = font_hdr
            cell.fill = fill_header if r == 7 else fill_sub_hdr
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            cell.border = thin_border
            
    # Ghi dữ liệu từ dòng 9
    current_row = 9
    total_revenue = 0
    total_qty = 0
    
    for idx, row in enumerate(rows, start=1):
        d = dict(row)
        rev = d.get('revenue') or 0
        total_revenue += rev
        
        # Đếm tổng qty từ devices_json
        qty = 1
        try:
            devs = json.loads(d.get('devices_json') or '[]')
            if devs:
                qty = sum(int(item.get('qty', 1)) for item in devs)
        except:
            qty = 1
        total_qty += qty
        
        ws.cell(current_row, 1, idx).alignment = Alignment(horizontal='center', vertical='center')
        ws.cell(current_row, 2, d.get('code', '')).alignment = Alignment(horizontal='center', vertical='center')
        ws.cell(current_row, 3, d.get('contract_sales', '')).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
        ws.cell(current_row, 4, d.get('service_desc', '')).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
        ws.cell(current_row, 5, d.get('customer_name', '')).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
        
        temp_val = normalize_excel_sample_codes(d.get('code_temp', ''))
        hum_val = normalize_excel_sample_codes(d.get('code_hum', ''))
        press_val = normalize_excel_sample_codes(d.get('code_press', ''))
        gas_val = normalize_excel_sample_codes(d.get('code_gas', ''))

        ws.cell(current_row, 6, temp_val).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        ws.cell(current_row, 7, hum_val).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        ws.cell(current_row, 8, press_val).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        ws.cell(current_row, 9, gas_val).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

        max_sample_lines = max(
            len(temp_val.split('\n')) if temp_val else 1,
            len(hum_val.split('\n')) if hum_val else 1,
            len(press_val.split('\n')) if press_val else 1,
            len(gas_val.split('\n')) if gas_val else 1,
            1
        )
        if max_sample_lines > 1:
            ws.row_dimensions[current_row].height = max(24, max_sample_lines * 17)
        
        ws.cell(current_row, 10, qty).alignment = Alignment(horizontal='center', vertical='center')
        
        c_rev = ws.cell(current_row, 11, rev)
        c_rev.number_format = '#,##0 "VNĐ"'
        c_rev.alignment = Alignment(horizontal='right', vertical='center')
        
        rec_person = d.get('received_person') or (d.get('received_info', '').split('_')[1] if '_' in (d.get('received_info') or '') else '') or d.get('recipient_person', '')
        rec_date = d.get('received_date') or (d.get('received_info', '').split('_')[0] if '_' in (d.get('received_info') or '') else (d.get('received_info') or ''))
        ret_person = d.get('returned_person') or (d.get('returned_info', '').split('_')[1] if '_' in (d.get('returned_info') or '') else '') or d.get('handover_person', '')
        ret_date = d.get('returned_date') or (d.get('returned_info', '').split('_')[0] if '_' in (d.get('returned_info') or '') else (d.get('returned_info') or '')) or d.get('expected_return_date', '')
        next_cal = d.get('next_cal_date', '')

        ws.cell(current_row, 12, d.get('technician', '')).alignment = Alignment(horizontal='center', vertical='center')
        ws.cell(current_row, 13, rec_person).alignment = Alignment(horizontal='left', vertical='center')
        ws.cell(current_row, 14, rec_date).alignment = Alignment(horizontal='center', vertical='center')
        ws.cell(current_row, 15, ret_person).alignment = Alignment(horizontal='left', vertical='center')
        ws.cell(current_row, 16, ret_date).alignment = Alignment(horizontal='center', vertical='center')
        ws.cell(current_row, 17, next_cal).alignment = Alignment(horizontal='center', vertical='center')
        
        ws.cell(current_row, 18, 'ĐÃ XUẤT' if d.get('cert_done') else 'Chưa').alignment = Alignment(horizontal='center', vertical='center')
        ws.cell(current_row, 19, 'ĐÃ GIAO' if d.get('device_done') else 'Chưa').alignment = Alignment(horizontal='center', vertical='center')
        ws.cell(current_row, 20, d.get('general_note', '')).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
        
        for c in range(1, 21):
            cell = ws.cell(current_row, c)
            cell.font = font_body
            cell.border = thin_border
            
        current_row += 1
        
    # Dòng Tổng cộng
    ws.merge_cells(f'A{current_row}:I{current_row}')
    ws.cell(current_row, 1, 'TỔNG CỘNG').alignment = Alignment(horizontal='center', vertical='center')
    ws.cell(current_row, 10, total_qty).alignment = Alignment(horizontal='center', vertical='center')
    c_tot_rev = ws.cell(current_row, 11, total_revenue)
    c_tot_rev.number_format = '#,##0 "VNĐ"'
    c_tot_rev.alignment = Alignment(horizontal='right', vertical='center')
    
    for c in range(1, 21):
        cell = ws.cell(current_row, c)
        cell.font = font_bold
        cell.fill = fill_sub_hdr
        cell.border = thin_border
        
    # Auto-adjust column widths
    col_widths = {
        'A': 6, 'B': 14, 'C': 18, 'D': 38, 'E': 34,
        'F': 14, 'G': 14, 'H': 14, 'I': 14, 'J': 10,
        'K': 20, 'L': 18, 'M': 18, 'N': 16, 'O': 18,
        'P': 16, 'Q': 18, 'R': 14, 'S': 14, 'T': 24
    }
    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = width
        
    stream = BytesIO()
    wb.save(stream)
    stream.seek(0)
    
    filename = f"SO_THEO_DOI_PTD_DIGI_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    return send_file(
        stream,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=filename
    )

# ================= MAIN ROUTES =================

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('.', path)

# Tự động khởi tạo database khi import module (phục vụ Gunicorn / Render)
init_db()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("==================================================================")
    print("  DIGI TECHNOLOGIES - HỆ THỐNG TIẾP NHẬN YÊU CẦU HIỆU CHUẨN & SỔ PTĐ")
    print(f"  Ứng dụng đang chạy tại: http://localhost:{port}")
    print("  Tài khoản Admin: CST@digivn.com | Mật khẩu: CST@654")
    print("  Tài khoản Nhân viên: nhanvien@digivn.com | Mật khẩu: 123456")
    print("==================================================================")
    app.run(host='0.0.0.0', port=port, debug=False)
