import urllib.request
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

base = 'http://127.0.0.1:5000'

# 1. Index
with urllib.request.urlopen(f'{base}/') as res:
    print('1. Index HTML status:', res.status)

# 2. Login Admin
req = urllib.request.Request(
    f'{base}/api/auth/login',
    data=json.dumps({'email': 'CST@digivn.com', 'password': 'CST@654'}).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
with urllib.request.urlopen(req) as res:
    login_res = json.loads(res.read().decode('utf-8'))
    print('2. Admin Login status:', res.status, login_res['user']['name'], '| Role:', login_res['user']['role'])

# 3. Next code
with urllib.request.urlopen(f'{base}/api/requests/next-code') as res:
    code_res = json.loads(res.read().decode('utf-8'))
    print('3. Next Code:', code_res['next_code'])

# 4. Get Requests
with urllib.request.urlopen(f'{base}/api/requests') as res:
    req_res = json.loads(res.read().decode('utf-8'))
    print('4. Total requests:', req_res['summary']['total_count'])
    print('   Total revenue:', req_res['summary']['total_revenue'], 'VND')
    print('   First request:', req_res['data'][0]['code'], '| Customer:', req_res['data'][0]['customer_name'][:35])

# 5. Export Excel
with urllib.request.urlopen(f'{base}/api/export-excel') as res:
    data = res.read()
    print('5. Export Excel status:', res.status, '| Size:', len(data), 'bytes')

print('\nALL TESTS PASSED WITH 100% SUCCESS!')
