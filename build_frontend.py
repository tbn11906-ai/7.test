import json

with open('assets_base64.json', 'r') as f:
    assets = json.load(f)

logo_b64 = f"data:image/png;base64,{assets['logo']}"
sig_b64 = f"data:image/png;base64,{assets['signature']}"

html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DIGI Technologies - Tiếp Nhận Yêu Cầu Hiệu Chuẩn & Sổ PTĐ</title>
    <!-- Font Awesome 6.6.0 Latest Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        digi: {{
                            DEFAULT: '#E30613',
                            hover: '#C00510',
                            dark: '#990000',
                            light: '#FEF2F2',
                            border: '#FECDD3'
                        }},
                        brand: {{
                            black: '#0F172A',
                            dark: '#1E293B',
                            gray: '#64748B'
                        }}
                    }},
                    fontFamily: {{
                        sans: ['Inter', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'sans-serif'],
                        mono: ['Consolas', 'Monaco', 'Courier New', 'monospace']
                    }},
                    fontSize: {{
                        'base': '15px'
                    }}
                }}
            }}
        }}
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #F8FAFC;
            color: #0F172A;
            font-size: 15px;
            line-height: 1.5;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}

        /* Glassmorphism Styles */
        .glass-auth {{
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(227, 6, 19, 0.2);
            box-shadow: 0 25px 60px -15px rgba(227, 6, 19, 0.2), 0 0 0 1px rgba(227, 6, 19, 0.1);
        }}

        /* Custom Scrollbars */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #F1F5F9;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #CBD5E1;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #94A3B8;
        }}

        /* Sticky Header for Tab 3 Table: Giữ cố định khi cuộn & hạn chế màu sắc */
        .sticky-header-row-1 {{
            position: sticky;
            top: 0;
            z-index: 20;
            background-color: #E2E8F0 !important;
        }}
        .sticky-header-row-2 {{
            position: sticky;
            top: 44px;
            z-index: 20;
            background-color: #F1F5F9 !important;
        }}

        /* Sample Code Item: Tách thành từng dòng riêng biệt, rõ ràng, dễ đối soát */
        .sample-code-item {{
            display: block;
            text-align: center;
            font-family: Consolas, Monaco, monospace;
            padding: 2px 6px;
            margin: 2px 0;
            background-color: #F8FAFC;
            border-radius: 5px;
            border: 1px solid #E2E8F0;
            white-space: nowrap;
        }}

        /* Print Layout Rules for BM.6.2.5 Form */
        @media print {{
            body {{
                background: #FFFFFF !important;
                margin: 0 !important;
                padding: 0 !important;
                font-size: 11pt !important;
            }}
            .no-print, header, nav, #app-navbar, #toast-container, #edit-modal {{
                display: none !important;
            }}
            #tab-print-content, #tab-2-content {{
                display: block !important;
                width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }}
            .print-a4-page {{
                box-shadow: none !important;
                border: none !important;
                margin: 0 auto !important;
                padding: 6mm 10mm !important;
                width: 100% !important;
                max-width: 100% !important;
                page-break-after: avoid !important;
                page-break-inside: avoid !important;
            }}
            @page {{
                size: A4 portrait;
                margin: 6mm 8mm;
            }}
        }}

        /* A4 Screen Preview Styling */
        .print-a4-page {{
            width: 210mm;
            min-height: 297mm;
            margin: 0 auto;
            background: #ffffff;
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.15), 0 2px 6px rgba(0, 0, 0, 0.08);
            padding: 10mm 14mm;
            position: relative;
            box-sizing: border-box;
            color: #000000;
            font-size: 10.5pt;
            line-height: 1.4;
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col antialiased select-none text-slate-800">

    <!-- ============================================================== -->
    <!-- 0. AUTHENTICATION GATEWAY (SECURED & NO AUTO-FILL)             -->
    <!-- ============================================================== -->
    <div id="auth-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/75 backdrop-blur-md transition-all duration-300">
        <div class="glass-auth w-full max-w-md rounded-3xl p-8 relative overflow-hidden text-center">
            <!-- Decorative Accent -->
            <div class="absolute -top-16 -right-16 w-48 h-48 bg-red-600/15 rounded-full blur-3xl pointer-events-none"></div>
            <div class="absolute -bottom-16 -left-16 w-48 h-48 bg-red-600/10 rounded-full blur-3xl pointer-events-none"></div>

            <!-- Clean Logo -->
            <div class="flex justify-center mb-5">
                <img src="{logo_b64}" alt="DIGI Technologies Logo" class="h-16 object-contain drop-shadow-sm">
            </div>

            <h2 class="text-xl font-black text-slate-900 tracking-tight uppercase">ĐĂNG NHẬP HỆ THỐNG</h2>
            <p class="text-xs font-semibold text-slate-500 mt-1">Vui lòng nhập tài khoản và mật khẩu được cấp để truy cập</p>

            <form id="login-form" class="mt-6 text-left space-y-4" onsubmit="handleLogin(event)" autocomplete="off">
                <div>
                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                        <i class="fa-solid fa-envelope mr-1.5 text-digi"></i>Email Nội Bộ
                    </label>
                    <div class="relative">
                        <input type="email" id="login-email" required value="" placeholder="Ví dụ: CST@digivn.com" autocomplete="off"
                            class="w-full px-4 py-3 text-sm bg-white border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-digi/50 focus:border-digi transition font-medium">
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                        <i class="fa-solid fa-lock mr-1.5 text-digi"></i>Mật Khẩu
                    </label>
                    <div class="relative">
                        <input type="password" id="login-password" required value="" placeholder="Nhập mật khẩu..." autocomplete="new-password"
                            class="w-full pl-4 pr-11 py-3 text-sm bg-white border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-digi/50 focus:border-digi transition font-medium">
                        <button type="button" onclick="togglePasswordVisibility()" class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-400 hover:text-slate-700">
                            <i id="eye-icon" class="fa-solid fa-eye text-sm"></i>
                        </button>
                    </div>
                </div>

                <div id="login-error" class="hidden p-3 rounded-xl bg-red-50 text-digi text-xs font-bold border border-red-200 text-center"></div>

                <button type="submit" id="btn-login-submit"
                    class="w-full py-3 px-5 bg-gradient-to-r from-digi to-red-600 hover:from-digi-hover hover:to-red-700 text-white text-sm font-extrabold rounded-xl shadow-lg shadow-red-500/25 transition duration-150 transform hover:-translate-y-0.5 active:translate-y-0 flex items-center justify-center space-x-2">
                    <i class="fa-solid fa-arrow-right-to-bracket text-base"></i>
                    <span>Xác Thực & Đăng Nhập</span>
                </button>
            </form>
            
            <p class="text-[11px] text-slate-400 mt-4 font-medium italic">
                <i class="fa-solid fa-shield-halved mr-1 text-slate-400"></i>Hệ thống bảo mật nội bộ DIGI Technologies
            </p>
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- MAIN APPLICATION WRAPPER                                       -->
    <!-- ============================================================== -->
    <div id="main-app" class="flex-1 flex flex-col">
        <!-- TOP NAVIGATION BAR -->
        <header id="app-navbar" class="no-print bg-white border-b border-slate-200 sticky top-0 z-40 shadow-xs">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-18">
                    <!-- Clean Brand Logo -->
                    <div class="flex items-center py-2">
                        <img src="{logo_b64}" alt="DIGI Logo" class="h-12 w-auto object-contain">
                    </div>

                    <!-- TÊN TAB ĐÃ CẬP NHẬT THEO YÊU CẦU: Tiếp Nhận | Phiếu Yêu Cầu | Sổ theo dõi -->
                    <nav class="flex space-x-1 sm:space-x-2 bg-slate-100 p-1.5 rounded-2xl">
                        <button id="nav-tab-1" onclick="switchTab(1)"
                            class="px-5 py-2.5 rounded-xl text-sm font-extrabold transition flex items-center space-x-2 bg-white text-digi shadow-xs">
                            <i class="fa-solid fa-file-pen text-base"></i>
                            <span>Tiếp Nhận</span>
                        </button>
                        <button id="nav-tab-2" onclick="switchTab(2)"
                            class="px-5 py-2.5 rounded-xl text-sm font-extrabold transition flex items-center space-x-2 text-slate-600 hover:text-slate-900">
                            <i class="fa-solid fa-file-invoice text-base"></i>
                            <span>Phiếu Yêu Cầu</span>
                        </button>
                        <button id="nav-tab-3" onclick="switchTab(3)"
                            class="px-5 py-2.5 rounded-xl text-sm font-extrabold transition flex items-center space-x-2 text-slate-600 hover:text-slate-900">
                            <i class="fa-solid fa-table-list text-base"></i>
                            <span>Sổ theo dõi</span>
                        </button>
                    </nav>

                    <!-- User Identity & Logout -->
                    <div class="flex items-center space-x-3">
                        <div class="text-right hidden sm:block">
                            <div class="text-sm font-bold text-slate-900" id="current-user-name">Quản trị viên CST</div>
                            <div class="flex items-center justify-end space-x-1.5 mt-0.5">
                                <span id="current-role-badge" class="inline-flex items-center px-2 py-0.5 rounded-md text-[11px] font-black bg-red-100 text-digi uppercase">
                                    ADMIN
                                </span>
                                <span class="text-xs text-slate-500 font-medium" id="current-user-email">CST@digivn.com</span>
                            </div>
                        </div>

                        <button onclick="handleLogout()" title="Đăng xuất"
                            class="p-2.5 rounded-xl text-slate-500 hover:text-digi hover:bg-red-50 border border-slate-200 transition">
                            <i class="fa-solid fa-right-from-bracket text-base"></i>
                        </button>
                    </div>
                </div>
            </div>
        </header>

        <!-- MAIN BODY CONTENT CONTAINER -->
        <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8">

            <!-- ============================================================== -->
            <!-- TAB 1: FORM TIẾP NHẬN                                          -->
            <!-- ============================================================== -->
            <div id="tab-1-content" class="space-y-6">
                <!-- Action Bar -->
                <div class="bg-white rounded-2xl p-5 shadow-xs border border-slate-200 flex flex-wrap items-center justify-between gap-4">
                    <div class="flex items-center space-x-3.5">
                        <div class="w-12 h-12 rounded-2xl bg-red-50 text-digi flex items-center justify-center text-xl font-black">
                            <i class="fa-solid fa-file-circle-plus"></i>
                        </div>
                        <div>
                            <div class="flex items-center space-x-3">
                                <h2 class="text-lg font-black text-slate-900">Tiếp Nhận Yêu Cầu Hiệu Chuẩn</h2>
                                <span id="form-code-badge" class="px-3 py-1 rounded-lg text-sm font-mono font-extrabold bg-slate-100 text-slate-800 border border-slate-300">
                                    HC.26.001
                                </span>
                            </div>
                            <p class="text-xs text-slate-500 font-medium mt-0.5">Nhập thông tin khách hàng, phương tiện đo và tính toán doanh số tự động theo thời gian thực</p>
                        </div>
                    </div>

                    <!-- Action buttons -->
                    <div class="flex flex-wrap items-center gap-2.5">
                        <button type="button" onclick="resetForm()"
                            class="px-4 py-2.5 text-xs font-bold text-slate-700 bg-white hover:bg-slate-100 border border-slate-300 rounded-xl transition flex items-center space-x-2">
                            <i class="fa-solid fa-rotate-left"></i>
                            <span>Làm mới form</span>
                        </button>

                        <button type="button" onclick="submitCalibrationForm(false)"
                            class="px-5 py-2.5 text-xs font-extrabold text-white bg-gradient-to-r from-digi to-red-600 hover:from-digi-hover hover:to-red-700 rounded-xl shadow-md shadow-red-500/25 transition flex items-center space-x-2">
                            <i class="fa-solid fa-floppy-disk text-sm"></i>
                            <span>LƯU VÀO SỔ & XEM BẢN IN</span>
                        </button>
                    </div>
                </div>

                <!-- Form Container -->
                <form id="calibration-form" onsubmit="event.preventDefault(); submitCalibrationForm(false);" class="space-y-6">

                    <!-- MỤC 1: THÔNG TIN KHÁCH HÀNG -->
                    <div class="bg-white rounded-2xl p-6 shadow-xs border border-slate-200">
                        <div class="flex items-center space-x-2.5 border-b border-slate-100 pb-3.5 mb-5">
                            <span class="flex items-center justify-center w-7 h-7 rounded-xl bg-red-100 text-digi text-sm font-black">1</span>
                            <h3 class="text-base font-black text-slate-900 uppercase tracking-wide">Thông Tin Khách Hàng</h3>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">Mã Phiếu Yêu Cầu <span class="text-digi">*</span></label>
                                <div class="flex space-x-1.5">
                                    <input type="text" id="req-code" required placeholder="HC.26.xxx" oninput="calculateEverything()"
                                        class="flex-1 px-3.5 py-2.5 text-sm font-mono font-bold bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 focus:border-digi">
                                    <button type="button" onclick="fetchNextCode()" title="Tự động sinh mã tiếp theo"
                                        class="px-3 py-2.5 text-sm font-bold bg-slate-100 hover:bg-slate-200 rounded-xl border border-slate-300 text-slate-700">
                                        <i class="fa-solid fa-arrows-rotate"></i>
                                    </button>
                                </div>
                            </div>

                            <div class="md:col-span-2">
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">Mã HĐ / Sales Phụ Trách</label>
                                <input type="text" id="req-contract" placeholder="Ví dụ: HĐ 21260006 - Mr. Lộc SV"
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 focus:border-digi font-medium">
                            </div>

                            <div class="md:col-span-2">
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">Tên Khách Hàng (Đầy đủ theo pháp nhân) <span class="text-digi">*</span></label>
                                <input type="text" id="req-customer-name" required placeholder="CÔNG TY TNHH / CỔ PHẦN..."
                                    class="w-full px-3.5 py-2.5 text-sm font-bold bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 focus:border-digi text-slate-900">
                            </div>

                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">Mã Số Thuế</label>
                                <input type="text" id="req-tax-code" placeholder="0312345678"
                                    class="w-full px-3.5 py-2.5 text-sm font-mono font-medium bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 focus:border-digi">
                            </div>

                            <div class="md:col-span-3">
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">Địa Chỉ</label>
                                <input type="text" id="req-customer-address" placeholder="Địa chỉ trụ sở / Nhà máy..."
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 focus:border-digi font-medium">
                            </div>

                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">Người Liên Hệ</label>
                                <input type="text" id="req-contact-person" placeholder="Họ và tên người liên hệ..."
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 focus:border-digi font-medium">
                            </div>

                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">SĐT Người Liên Hệ</label>
                                <input type="text" id="req-contact-phone" placeholder="0908 xxx xxx"
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 focus:border-digi font-medium">
                            </div>

                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">Email</label>
                                <input type="email" id="req-contact-email" placeholder="contact@company.com"
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 focus:border-digi font-medium">
                            </div>
                        </div>
                    </div>

                    <!-- MỤC 2: THÔNG TIN PHƯƠNG TIỆN ĐO & MÃ MẪU -->
                    <div class="bg-white rounded-2xl p-6 shadow-xs border border-slate-200">
                        <div class="flex items-center justify-between border-b border-slate-100 pb-3.5 mb-5">
                            <div class="flex items-center space-x-2.5">
                                <span class="flex items-center justify-center w-7 h-7 rounded-xl bg-red-100 text-digi text-sm font-black">2</span>
                                <h3 class="text-base font-black text-slate-900 uppercase tracking-wide">Thông Tin Phương Tiện Đo</h3>
                            </div>
                            <button type="button" onclick="addDeviceRow()"
                                class="px-3.5 py-1.5 text-xs font-extrabold text-digi bg-red-50 hover:bg-red-100 rounded-xl border border-red-200 transition flex items-center space-x-1.5">
                                <i class="fa-solid fa-plus"></i>
                                <span>Thêm dòng thiết bị</span>
                            </button>
                        </div>

                        <!-- Danh sách thiết bị -->
                        <div class="overflow-x-auto rounded-xl border border-slate-200 mb-5">
                            <table class="w-full text-left text-sm text-slate-700" id="device-table">
                                <thead class="bg-slate-50 text-xs font-black text-slate-700 uppercase border-b border-slate-200">
                                    <tr>
                                        <th class="p-3 w-14 text-center">STT</th>
                                        <th class="p-3">Tên Đối Tượng Hiệu Chuẩn</th>
                                        <th class="p-3 w-48">Đặc Tính Kỹ Thuật</th>
                                        <th class="p-3 w-28 text-center">Số Lượng</th>
                                        <th class="p-3">Tình Trạng Khi Nhận</th>
                                        <th class="p-3 w-16 text-center">Xóa</th>
                                    </tr>
                                </thead>
                                <tbody id="device-tbody" class="divide-y divide-slate-200 bg-white">
                                    <!-- Rendered dynamically -->
                                </tbody>
                            </table>
                        </div>

                        <!-- KHỐI MÃ MẪU: TỰ ĐỘNG SINH & HIỂN THỊ TÁCH TỪNG DÒNG THEO SỐ LƯỢNG -->
                        <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200">
                            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                                <div>
                                    <span class="text-sm font-black text-slate-900 uppercase tracking-wider">
                                        <i class="fa-solid fa-tags mr-1.5 text-digi"></i>MÃ MẪU PHÂN THEO NHÓM:
                                    </span>
                                    <span class="text-xs text-slate-500 ml-1 font-medium">(Tự động sinh theo Số lượng, mỗi mã 1 dòng riêng biệt)</span>
                                </div>
                                <button type="button" onclick="autoAllocateSampleCodes(true)"
                                    class="px-3 py-1.5 text-xs font-bold text-digi hover:text-white bg-red-50 hover:bg-digi border border-red-200 rounded-xl transition flex items-center space-x-1">
                                    <i class="fa-solid fa-wand-magic-sparkles"></i>
                                    <span>Tự động sinh lại mã mẫu</span>
                                </button>
                            </div>

                            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                                <div>
                                    <div class="flex items-center justify-between mb-1.5">
                                        <label class="block text-xs font-bold text-slate-700">1. Nhiệt: HC.1.yy.xxx</label>
                                        <span id="badge-count-temp" class="text-[11px] font-mono font-medium text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md">0 mã</span>
                                    </div>
                                    <textarea id="code-temp" rows="2" placeholder="HC.1.26.xxx&#10;HC.1.26.yyy" oninput="updateSampleCodeBadges()"
                                        class="w-full px-3 py-2 text-xs font-mono font-semibold bg-white border border-slate-300 rounded-xl focus:ring-1 focus:ring-digi leading-relaxed resize-y"></textarea>
                                </div>
                                <div>
                                    <div class="flex items-center justify-between mb-1.5">
                                        <label class="block text-xs font-bold text-slate-700">2. Nhiệt ẩm: HC.2.yy.xxx</label>
                                        <span id="badge-count-hum" class="text-[11px] font-mono font-medium text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md">0 mã</span>
                                    </div>
                                    <textarea id="code-hum" rows="2" placeholder="HC.2.26.xxx&#10;HC.2.26.yyy" oninput="updateSampleCodeBadges()"
                                        class="w-full px-3 py-2 text-xs font-mono font-semibold bg-white border border-slate-300 rounded-xl focus:ring-1 focus:ring-digi leading-relaxed resize-y"></textarea>
                                </div>
                                <div>
                                    <div class="flex items-center justify-between mb-1.5">
                                        <label class="block text-xs font-bold text-slate-700">3. Áp: HC.3.yy.xxx</label>
                                        <span id="badge-count-press" class="text-[11px] font-mono font-medium text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md">0 mã</span>
                                    </div>
                                    <textarea id="code-press" rows="2" placeholder="HC.3.26.xxx&#10;HC.3.26.yyy" oninput="updateSampleCodeBadges()"
                                        class="w-full px-3 py-2 text-xs font-mono font-semibold bg-white border border-slate-300 rounded-xl focus:ring-1 focus:ring-digi leading-relaxed resize-y"></textarea>
                                </div>
                                <div>
                                    <div class="flex items-center justify-between mb-1.5">
                                        <label class="block text-xs font-bold text-slate-700">4. Khí: HC.4.yy.xxx</label>
                                        <span id="badge-count-gas" class="text-[11px] font-mono font-medium text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md">0 mã</span>
                                    </div>
                                    <textarea id="code-gas" rows="2" placeholder="HC.4.26.xxx&#10;HC.4.26.yyy" oninput="updateSampleCodeBadges()"
                                        class="w-full px-3 py-2 text-xs font-mono font-semibold bg-white border border-slate-300 rounded-xl focus:ring-1 focus:ring-digi leading-relaxed resize-y"></textarea>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- MỤC 3: QUY TRÌNH HIỆU CHUẨN SỬ DỤNG (ĐẦY ĐỦ 'QTHC') -->
                    <div class="bg-white rounded-2xl p-6 shadow-xs border border-slate-200">
                        <div class="flex items-center space-x-2.5 border-b border-slate-100 pb-3.5 mb-4">
                            <span class="flex items-center justify-center w-7 h-7 rounded-xl bg-red-100 text-digi text-sm font-black">3</span>
                            <h3 class="text-base font-black text-slate-900 uppercase tracking-wide">Quy Trình Hiệu Chuẩn Sử Dụng</h3>
                        </div>
                        <p class="text-xs text-slate-500 mb-4">Tích chọn để tự động đồng bộ vào Mục 7 của Phiếu Yêu Cầu Hiệu Chuẩn BM.6.2.5:</p>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm" id="procedures-container">
                            <label class="flex items-start space-x-3 p-3.5 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer transition">
                                <input type="checkbox" name="procedure" value="DIGI.QT.HC.012023 QTHC Nhiệt kế chỉ thị hiện số và tương tự"
                                    class="mt-1 rounded text-digi focus:ring-digi h-4 w-4">
                                <span class="font-medium text-slate-800">
                                    <strong class="font-extrabold text-slate-900">DIGI.QT.HC.012023</strong> QTHC Nhiệt kế chỉ thị hiện số và tương tự
                                </span>
                            </label>

                            <label class="flex items-start space-x-3 p-3.5 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer transition">
                                <input type="checkbox" name="procedure" value="DIGI.QT.HC.022023 QTHC Nhiệt ẩm kế không khí"
                                    class="mt-1 rounded text-digi focus:ring-digi h-4 w-4">
                                <span class="font-medium text-slate-800">
                                    <strong class="font-extrabold text-slate-900">DIGI.QT.HC.022023</strong> QTHC Nhiệt ẩm kế không khí
                                </span>
                            </label>

                            <label class="flex items-start space-x-3 p-3.5 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer transition">
                                <input type="checkbox" name="procedure" value="DIGI.QT.HC.032023 QTHC Áp kế chênh áp kiểu hiện số"
                                    class="mt-1 rounded text-digi focus:ring-digi h-4 w-4">
                                <span class="font-medium text-slate-800">
                                    <strong class="font-extrabold text-slate-900">DIGI.QT.HC.032023</strong> QTHC Áp kế chênh áp kiểu hiện số
                                </span>
                            </label>

                            <label class="flex items-start space-x-3 p-3.5 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer transition">
                                <input type="checkbox" name="procedure" value="DIGI.QT.HC.042023 QTHC PTĐ Nồng độ khí"
                                    class="mt-1 rounded text-digi focus:ring-digi h-4 w-4">
                                <span class="font-medium text-slate-800">
                                    <strong class="font-extrabold text-slate-900">DIGI.QT.HC.042023</strong> QTHC PTĐ Nồng độ khí
                                </span>
                            </label>
                        </div>
                    </div>

                    <!-- MỤC 4: BẢNG CHỌN THÔNG SỐ HIỆU CHUẨN (BỎ CHỮ 'CHIẾC' Ở NHÓM ĐO LƯỜNG THEO YÊU CẦU) -->
                    <div class="bg-gradient-to-br from-white to-red-50/40 rounded-2xl p-6 shadow-xs border-2 border-red-200">
                        <div class="flex items-center justify-between border-b border-red-100 pb-3.5 mb-5">
                            <div class="flex items-center space-x-2.5">
                                <span class="flex items-center justify-center w-7 h-7 rounded-xl bg-digi text-white text-sm font-black">4</span>
                                <h3 class="text-base font-black text-slate-900 uppercase tracking-wide">
                                    Bảng Chọn Thông Số Hiệu Chuẩn & Tính Doanh Số (Chưa VAT)
                                </h3>
                            </div>
                            <span class="text-xs font-black text-digi bg-red-100 px-3 py-1 rounded-full uppercase tracking-wider">
                                <i class="fa-solid fa-calculator mr-1"></i>Tự động tính thời gian thực
                            </span>
                        </div>

                        <!-- 2 Cột: Thông số Khí & Đo lường -->
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5 mb-5">
                            <!-- Khí Thải (1.500.000 VNĐ / chỉ tiêu) -->
                            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs">
                                <div class="flex items-center justify-between mb-3">
                                    <div>
                                        <h4 class="text-sm font-black text-slate-900 uppercase">Nhóm Khí Thải</h4>
                                        <span class="text-xs font-bold text-digi">1.500.000 VNĐ / mỗi chỉ tiêu khí</span>
                                    </div>
                                    <div class="space-x-2 text-xs">
                                        <button type="button" onclick="selectAllGases(true)" class="font-bold text-digi hover:underline">Chọn hết</button>
                                        <span class="text-slate-300">|</span>
                                        <button type="button" onclick="selectAllGases(false)" class="font-bold text-slate-500 hover:underline">Bỏ chọn</button>
                                    </div>
                                </div>

                                <div class="grid grid-cols-3 gap-3 mt-3">
                                    <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:border-digi cursor-pointer text-sm font-extrabold transition bg-slate-50/50">
                                        <input type="checkbox" name="gas_param" value="O2" onchange="calculateEverything()" class="rounded text-digi focus:ring-digi h-4 w-4">
                                        <span>O2</span>
                                    </label>
                                    <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:border-digi cursor-pointer text-sm font-extrabold transition bg-slate-50/50">
                                        <input type="checkbox" name="gas_param" value="CO" onchange="calculateEverything()" class="rounded text-digi focus:ring-digi h-4 w-4">
                                        <span>CO</span>
                                    </label>
                                    <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:border-digi cursor-pointer text-sm font-extrabold transition bg-slate-50/50">
                                        <input type="checkbox" name="gas_param" value="CO2" onchange="calculateEverything()" class="rounded text-digi focus:ring-digi h-4 w-4">
                                        <span>CO2</span>
                                    </label>
                                    <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:border-digi cursor-pointer text-sm font-extrabold transition bg-slate-50/50">
                                        <input type="checkbox" name="gas_param" value="NO" onchange="calculateEverything()" class="rounded text-digi focus:ring-digi h-4 w-4">
                                        <span>NO</span>
                                    </label>
                                    <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:border-digi cursor-pointer text-sm font-extrabold transition bg-slate-50/50">
                                        <input type="checkbox" name="gas_param" value="NO2" onchange="calculateEverything()" class="rounded text-digi focus:ring-digi h-4 w-4">
                                        <span>NO2</span>
                                    </label>
                                    <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:border-digi cursor-pointer text-sm font-extrabold transition bg-slate-50/50">
                                        <input type="checkbox" name="gas_param" value="SO2" onchange="calculateEverything()" class="rounded text-digi focus:ring-digi h-4 w-4">
                                        <span>SO2</span>
                                    </label>
                                </div>
                            </div>

                            <!-- Nhóm Đo Lường (BỎ CHỮ CHIẾC Ở NHIỆT ẨM THEO YÊU CẦU) -->
                            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs">
                                <div class="flex items-center justify-between mb-3">
                                    <h4 class="text-sm font-black text-slate-900 uppercase">Nhóm Đo Lường</h4>
                                    <span class="text-xs font-semibold text-slate-500">Đơn giá chuẩn hệ thống</span>
                                </div>

                                <div class="space-y-2.5 mt-3 text-sm">
                                    <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 hover:border-digi cursor-pointer transition bg-slate-50/50">
                                        <div class="flex items-center space-x-2.5">
                                            <input type="checkbox" id="param-temp" onchange="calculateEverything()" class="rounded text-digi focus:ring-digi h-4 w-4">
                                            <span class="font-extrabold text-slate-800">NHIỆT ĐỘ</span>
                                        </div>
                                        <span class="font-mono font-bold text-slate-700 text-sm">500.000 VNĐ</span>
                                    </label>

                                    <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 hover:border-digi cursor-pointer transition bg-slate-50/50">
                                        <div class="flex items-center space-x-2.5">
                                            <input type="checkbox" id="param-press" onchange="calculateEverything()" class="rounded text-digi focus:ring-digi h-4 w-4">
                                            <span class="font-extrabold text-slate-800">CHÊNH ÁP / ÁP SUẤT</span>
                                        </div>
                                        <span class="font-mono font-bold text-slate-700 text-sm">500.000 VNĐ</span>
                                    </label>

                                    <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 hover:border-digi cursor-pointer transition bg-slate-50/50">
                                        <div class="flex items-center space-x-2.5">
                                            <input type="checkbox" id="param-hum" onchange="calculateEverything()" class="rounded text-digi focus:ring-digi h-4 w-4">
                                            <span class="font-extrabold text-slate-800">NHIỆT ẨM</span>
                                        </div>
                                        <!-- BỎ CHỮ 'chiếc' theo yêu cầu -->
                                        <span class="font-mono font-bold text-slate-700 text-sm">750.000 VNĐ</span>
                                    </label>
                                </div>
                            </div>
                        </div>

                        <!-- Khối Hiển thị Tự động Sinh Nội Dung & Doanh Số -->
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 bg-white p-5 rounded-2xl border border-red-200">
                            <!-- Mô tả dịch vụ sinh tự động -->
                            <div class="md:col-span-2">
                                <label class="block text-xs font-bold text-slate-800 mb-1.5 uppercase">
                                    <i class="fa-solid fa-pen-nib mr-1 text-digi"></i>Mô Tả Dịch Vụ Hiệu Chuẩn (Đồng bộ vào Mục 8 & Sổ theo dõi):
                                </label>
                                <textarea id="service-description" rows="3"
                                    class="w-full p-3 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 font-medium text-slate-900"
                                    placeholder="Nội dung tự động sinh từ thông số đo..."></textarea>
                            </div>

                            <!-- Thẻ Doanh số To Nổi Bật -->
                            <div class="bg-gradient-to-br from-digi to-red-700 rounded-2xl p-5 text-white flex flex-col justify-between shadow-lg shadow-red-500/25">
                                <div>
                                    <span class="text-[11px] font-black uppercase tracking-widest text-red-100">DOANH SỐ (CHƯA VAT)</span>
                                    <div class="text-3xl font-black tracking-tight mt-1.5" id="revenue-display">
                                        0 VNĐ
                                    </div>
                                    <input type="hidden" id="calculated-revenue" value="0">
                                </div>
                                <div class="text-xs text-red-100 font-mono mt-3" id="revenue-formula">
                                    Chưa chọn thông số hiệu chuẩn
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- MỤC 5: SẮP XẾP LẠI THEO THỨ TỰ YÊU CẦU:
                         Ngày nhận PTĐ, Ngày trả kết quả dự kiến, Người Bàn giao, người nhận (VÀ BỎ MỤC NGÀY HIỆU CHUẨN TIẾP THEO) -->
                    <div class="bg-white rounded-2xl p-6 shadow-xs border border-slate-200">
                        <div class="flex items-center space-x-2.5 border-b border-slate-100 pb-3.5 mb-5">
                            <span class="flex items-center justify-center w-7 h-7 rounded-xl bg-red-100 text-digi text-sm font-black">5</span>
                            <h3 class="text-base font-black text-slate-900 uppercase tracking-wide">Điều Khoản Thực Hiện & Bàn Giao</h3>
                        </div>

                        <!-- 4 Yêu cầu hiệu chuẩn -->
                        <div class="mb-5">
                            <label class="block text-xs font-bold text-slate-700 mb-2.5 uppercase">Yêu Cầu Hiệu Chuẩn (Mục 9 Phiếu Yêu Cầu):</label>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm">
                                <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer">
                                    <input type="checkbox" id="req-adjust" class="rounded text-digi focus:ring-digi h-4 w-4">
                                    <span class="text-slate-800 font-medium">Hiệu chuẩn có hiệu chỉnh</span>
                                </label>

                                <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer">
                                    <input type="checkbox" id="req-uncertainty" checked class="rounded text-digi focus:ring-digi h-4 w-4">
                                    <span class="text-slate-900 font-extrabold">Công bố độ không đảm bảo đo (Mặc định)</span>
                                </label>

                                <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer">
                                    <input type="checkbox" id="req-compliance" class="rounded text-digi focus:ring-digi h-4 w-4">
                                    <span class="text-slate-800 font-medium">Tuyên bố sự phù hợp</span>
                                </label>

                                <label class="flex items-center space-x-2.5 p-3 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer">
                                    <input type="checkbox" id="req-next-date" checked class="rounded text-digi focus:ring-digi h-4 w-4">
                                    <span class="text-slate-900 font-extrabold">Ghi ngày đề nghị hiệu chuẩn tiếp theo (Mặc định)</span>
                                </label>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 mb-5">
                            <!-- 1. Ngày nhận PTĐ -->
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">
                                    <i class="fa-regular fa-calendar-plus mr-1 text-digi"></i>Ngày nhận PTĐ
                                </label>
                                <input type="text" id="req-received-date" placeholder="DD/MM/YYYY (Ví dụ: 29/10/2026)"
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 font-medium">
                            </div>

                            <!-- 2. Ngày trả kết quả dự kiến -->
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">
                                    <i class="fa-regular fa-calendar-check mr-1 text-digi"></i>Ngày trả kết quả dự kiến
                                </label>
                                <input type="date" id="req-expected-return"
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 font-medium">
                            </div>

                            <!-- 3. Người Bàn giao -->
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">
                                    <i class="fa-solid fa-hand-holding-hand mr-1 text-digi"></i>Người Bàn giao
                                </label>
                                <input type="text" id="req-handover-person" placeholder="Tên người bàn giao..."
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 font-medium">
                            </div>

                            <!-- 4. Người nhận -->
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">
                                    <i class="fa-solid fa-user-check mr-1 text-digi"></i>Người nhận
                                </label>
                                <input type="text" id="req-recipient-person" placeholder="Tên người nhận..."
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 font-medium">
                            </div>

                            <!-- Nhân viên hiệu chuẩn -->
                            <div class="md:col-span-2">
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">
                                    <i class="fa-solid fa-user-gear mr-1 text-digi"></i>Nhân viên hiệu chuẩn (NVHC)
                                </label>
                                <input type="text" id="req-technician" value="Nguyễn Minh Tú" placeholder="Họ tên KTV (Ví dụ: Nguyễn Minh Tú)"
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 font-bold">
                            </div>

                            <!-- Hình thức trả kết quả -->
                            <div class="md:col-span-2">
                                <label class="block text-xs font-bold text-slate-700 mb-2 uppercase">Hình Thức Trả Kết Quả</label>
                                <div class="flex space-x-6 pt-1 text-sm">
                                    <label class="flex items-center space-x-2 cursor-pointer font-medium">
                                        <input type="radio" name="return_method" value="VP" class="text-digi focus:ring-digi">
                                        <span>Trả trực tiếp tại VP</span>
                                    </label>
                                    <label class="flex items-center space-x-2 cursor-pointer font-extrabold text-slate-900">
                                        <input type="radio" name="return_method" value="CHUYEN_PHAT" checked class="text-digi focus:ring-digi">
                                        <span>Gửi chuyển phát</span>
                                    </label>
                                </div>
                            </div>

                            <div class="md:col-span-2 lg:col-span-4">
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">Ghi Chú Về Phụ Tùng Kèm Theo (Mục 13)</label>
                                <input type="text" id="req-accessories" value="Cáp nguồn, đầu đo theo máy" placeholder="Cáp nguồn, vali, đầu đo..."
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 font-medium">
                            </div>

                            <div class="md:col-span-2 lg:col-span-4">
                                <label class="block text-xs font-bold text-slate-700 mb-1.5 uppercase">Lưu Ý Thêm Về PTĐ & Các Yêu Cầu Khác (Mục 14 & Ghi chú sổ)</label>
                                <input type="text" id="req-notes" placeholder="Yêu cầu kiểm định, bảo dưỡng, nơi lắp đặt..."
                                    class="w-full px-3.5 py-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 font-medium">
                            </div>
                        </div>

                        <!-- Submit Buttons -->
                        <div class="pt-5 border-t border-slate-200 flex flex-wrap items-center justify-end gap-3">
                            <button type="button" onclick="resetForm()"
                                class="px-5 py-3 text-sm font-bold text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-xl transition">
                                <i class="fa-solid fa-rotate-left mr-1.5"></i>Làm Mới
                            </button>
                            <button type="submit"
                                class="px-7 py-3 text-sm font-extrabold text-white bg-gradient-to-r from-digi to-red-600 hover:from-digi-hover hover:to-red-700 rounded-xl shadow-lg shadow-red-500/25 transition duration-150 transform hover:-translate-y-0.5 flex items-center space-x-2">
                                <i class="fa-solid fa-floppy-disk text-base"></i>
                                <span>LƯU VÀO SỔ THEO DÕI & CHUYỂN SANG IN PHIẾU</span>
                            </button>
                        </div>
                    </div>
                </form>
            </div>

            <!-- ============================================================== -->
            <!-- TAB 2: XUẤT & IN PHIẾU YÊU CẦU HIỆU CHUẨN (BM.6.2.5 NGAY HÀNG) -->
            <!-- ============================================================== -->
            <div id="tab-2-content" class="hidden space-y-4">
                <!-- Control Bar for Printing / Selecting Record -->
                <div class="no-print bg-white rounded-2xl p-4 shadow-xs border border-slate-200 flex flex-wrap items-center justify-between gap-3">
                    <div class="flex items-center space-x-3">
                        <label class="text-sm font-bold text-slate-700"><i class="fa-solid fa-list-check mr-1.5 text-digi"></i>Chọn phiếu cần in:</label>
                        <select id="print-selector" onchange="loadRequestToPrint(this.value)"
                            class="px-3.5 py-2 text-sm font-bold bg-slate-50 border border-slate-300 rounded-xl focus:ring-1 focus:ring-digi">
                            <!-- Populated by JS -->
                        </select>
                        <span id="print-code-indicator" class="text-sm font-mono font-black text-digi bg-red-50 px-3 py-1 rounded-lg border border-red-200">
                            HC.26.001
                        </span>
                    </div>

                    <div class="flex items-center space-x-2.5">
                        <button type="button" onclick="switchTab(1)"
                            class="px-4 py-2 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-xl transition flex items-center space-x-1.5">
                            <i class="fa-solid fa-pen-to-square"></i>
                            <span>Sửa phiếu này ở Tab Tiếp Nhận</span>
                        </button>
                        <button type="button" onclick="window.print()"
                            class="px-6 py-2.5 text-sm font-extrabold text-white bg-gradient-to-r from-digi to-red-600 hover:from-digi-hover hover:to-red-700 rounded-xl shadow-md shadow-red-500/25 transition flex items-center space-x-2">
                            <i class="fa-solid fa-print text-base"></i>
                            <span>IN PHIẾU NGAY (PRINT / PDF)</span>
                        </button>
                    </div>
                </div>

                <!-- A4 PREVIEW CONTAINER -->
                <div class="flex justify-center pb-12">
                    <div id="print-sheet" class="print-a4-page font-sans text-black">

                        <!-- HEADER 3 CỘT CĂN ĐỀU TUYỆT ĐỐI -->
                        <div class="flex items-center border-b-2 border-black pb-2.5 mb-3">
                            <!-- Cột Trái: Logo DIGI Technologies mới -->
                            <div class="w-1/4 flex items-center pr-2">
                                <img src="{logo_b64}" alt="DIGI Logo" class="h-11 w-auto object-contain">
                            </div>

                            <!-- Cột Giữa: Tiêu đề in hoa đậm -->
                            <div class="w-2/4 text-center px-1">
                                <h1 class="text-[14pt] font-black uppercase tracking-wider text-black">
                                    PHIẾU YÊU CẦU HIỆU CHUẨN
                                </h1>
                                <p class="text-[10pt] font-extrabold text-gray-900 mt-0.5 tracking-tight" id="p-form-code-title">
                                    Số: HC.26.001
                                </p>
                            </div>

                            <!-- Cột Phải: Bảng Kiểm soát Tài liệu ISO BM.6.2.5 -->
                            <div class="w-1/4 pl-2 flex items-center justify-end">
                                <table class="text-[8pt] border-collapse border border-black w-full text-left">
                                    <tbody>
                                        <tr><td class="border border-black px-1.5 py-0.5 font-bold w-20">Mã số:</td><td class="border border-black px-1.5 py-0.5 font-mono font-bold">BM.6.2.5</td></tr>
                                        <tr><td class="border border-black px-1.5 py-0.5 font-bold">Lần sửa đổi:</td><td class="border border-black px-1.5 py-0.5">00</td></tr>
                                        <tr><td class="border border-black px-1.5 py-0.5 font-bold">Lần ban hành:</td><td class="border border-black px-1.5 py-0.5">01</td></tr>
                                        <tr><td class="border border-black px-1.5 py-0.5 font-bold">Ngày SĐ/BH:</td><td class="border border-black px-1.5 py-0.5 font-mono">05/12/2022</td></tr>
                                        <tr><td class="border border-black px-1.5 py-0.5 font-bold">Trang:</td><td class="border border-black px-1.5 py-0.5">1/1</td></tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        <!-- THÂN PHIẾU: 14 MỤC CHUẨN ISO CĂN HÀNG THẲNG TẮP -->
                        <div class="text-[9.5pt] leading-normal space-y-1.5">

                            <!-- 1. Tên khách hàng -->
                            <div class="flex items-baseline">
                                <span class="font-bold w-44 shrink-0">1. Tên khách hàng:</span>
                                <span class="flex-1 font-bold uppercase text-black" id="p-customer-name">CÔNG TY TNHH...</span>
                            </div>

                            <!-- 2. Địa chỉ -->
                            <div class="flex items-baseline">
                                <span class="font-bold w-44 shrink-0">2. Địa chỉ:</span>
                                <span class="flex-1" id="p-customer-address">Việt Nam</span>
                            </div>

                            <!-- 3. Mã số thuế -->
                            <div class="flex items-baseline">
                                <span class="font-bold w-44 shrink-0">3. Mã số thuế:</span>
                                <span class="flex-1 font-mono font-bold" id="p-customer-tax">0312345678</span>
                            </div>

                            <!-- 4. Người liên hệ & SĐT -->
                            <div class="grid grid-cols-2 gap-4">
                                <div class="flex items-baseline">
                                    <span class="font-bold w-44 shrink-0">4. Người liên hệ:</span>
                                    <span class="flex-1 font-medium" id="p-contact-person">Nguyễn Văn A</span>
                                </div>
                                <div class="flex items-baseline">
                                    <span class="font-bold w-32 shrink-0">SĐT người LH:</span>
                                    <span class="flex-1 font-mono font-bold" id="p-contact-phone">0908 123 456</span>
                                </div>
                            </div>

                            <!-- 5. Email -->
                            <div class="flex items-baseline">
                                <span class="font-bold w-44 shrink-0">5. Email:</span>
                                <span class="flex-1 font-medium" id="p-contact-email">contact@company.com</span>
                            </div>

                            <!-- 6. Thông tin thiết bị -->
                            <div class="pt-1">
                                <span class="font-bold block mb-1">6. Thông tin thiết bị:</span>
                                <table class="w-full text-left border-collapse border border-black text-[9pt]">
                                    <thead>
                                        <tr class="bg-gray-100 font-bold text-center">
                                            <th class="border border-black p-1.5 w-10">STT</th>
                                            <th class="border border-black p-1.5">Tên đối tượng hiệu chuẩn</th>
                                            <th class="border border-black p-1.5 w-36">Đặc tính kỹ thuật</th>
                                            <th class="border border-black p-1.5 w-16 text-center">Số lượng</th>
                                            <th class="border border-black p-1.5 w-44">Tình trạng thiết bị</th>
                                        </tr>
                                    </thead>
                                    <tbody id="p-devices-tbody">
                                        <!-- Dynamically generated rows -->
                                    </tbody>
                                </table>
                            </div>

                            <!-- 7. Quy trình hiệu chuẩn sử dụng -->
                            <div class="pt-1">
                                <span class="font-bold block mb-0.5">7. Quy trình hiệu chuẩn sử dụng:</span>
                                <div class="pl-4 text-[9pt] text-gray-900 space-y-0.5" id="p-procedures-list">
                                    <!-- Procedures list -->
                                </div>
                            </div>

                            <!-- 8. Mô tả dịch vụ hiệu chuẩn -->
                            <div class="pt-1">
                                <span class="font-bold block mb-0.5">8. Mô tả dịch vụ hiệu chuẩn:</span>
                                <div class="pl-4 text-[9pt] font-semibold text-gray-900" id="p-service-desc">
                                    Dịch vụ hiệu chuẩn Testo 350 tại các thông số: O2, CO, NO, NO2, SO2; NHIỆT ĐỘ, CHÊNH ÁP.
                                </div>
                            </div>

                            <!-- 9. Yêu cầu hiệu chuẩn -->
                            <div class="pt-1">
                                <span class="font-bold block mb-0.5">9. Yêu cầu hiệu chuẩn:</span>
                                <div class="grid grid-cols-2 gap-x-6 gap-y-0.5 pl-4 text-[9pt]">
                                    <div class="flex items-center space-x-2" id="p-req-adjust">
                                        <span class="font-mono">[ ]</span><span>Hiệu chuẩn có hiệu chỉnh</span>
                                    </div>
                                    <div class="flex items-center space-x-2" id="p-req-uncertainty">
                                        <span class="font-mono font-bold">[x]</span><span class="font-bold">Công bố độ không đảm bảo đo</span>
                                    </div>
                                    <div class="flex items-center space-x-2" id="p-req-compliance">
                                        <span class="font-mono">[ ]</span><span>Tuyên bố sự phù hợp</span>
                                    </div>
                                    <div class="flex items-center space-x-2" id="p-req-next-date">
                                        <span class="font-mono font-bold">[x]</span><span class="font-bold">Ghi ngày đề nghị hiệu chuẩn tiếp theo</span>
                                    </div>
                                </div>
                            </div>

                            <!-- 10. Hình thức trả kết quả -->
                            <div class="pt-1">
                                <span class="font-bold block mb-0.5">10. Hình thức trả kết quả:</span>
                                <div class="flex space-x-10 pl-4 text-[9pt]" id="p-return-method">
                                    <span>[ ] Trả trực tiếp tại văn phòng hiệu chuẩn</span>
                                    <span class="font-bold">[x] Gửi chuyển phát</span>
                                </div>
                            </div>

                            <!-- 11. Ngày trả kết quả -->
                            <div class="flex items-baseline">
                                <span class="font-bold w-64 shrink-0">11. Ngày trả kết quả (Dự kiến):</span>
                                <span class="flex-1 font-bold" id="p-expected-date">Theo thỏa thuận</span>
                            </div>

                            <!-- 12. Chi phí hiệu chuẩn -->
                            <div class="flex items-baseline">
                                <span class="font-bold w-64 shrink-0">12. Chi phí hiệu chuẩn:</span>
                                <span class="flex-1 font-bold text-[10.5pt] text-black">
                                    <span id="p-cost">0 VNĐ</span>
                                    <span class="text-[8.5pt] font-normal italic text-gray-700 ml-1.5">(Chưa bao gồm thuế VAT)</span>
                                </span>
                            </div>

                            <!-- 13. Ghi chú về phụ tùng kèm theo -->
                            <div class="flex items-baseline">
                                <span class="font-bold w-64 shrink-0">13. Ghi chú về phụ tùng kèm theo:</span>
                                <span class="flex-1" id="p-accessories">Cáp nguồn, đầu đo theo máy</span>
                            </div>

                            <!-- 14. Lưu ý thêm -->
                            <div class="flex items-baseline">
                                <span class="font-bold w-64 shrink-0">14. Lưu ý thêm về PTĐ và yêu cầu khác:</span>
                                <span class="flex-1" id="p-general-note">Không có</span>
                            </div>
                        </div>

                        <!-- LƯU Ý BẢO MẬT & CAM KẾT (3 ĐIỀU KHOẢN) -->
                        <div class="mt-4 pt-2.5 border-t border-gray-400 text-[8pt] text-gray-700 leading-tight">
                            <span class="font-bold text-black uppercase">Lưu ý:</span>
                            <ul class="list-disc pl-5 space-y-0.5 mt-0.5">
                                <li>Trong trường hợp có thay đổi các thông tin yêu cầu sẽ được 02 bên thảo luận thống nhất để lập lại bản yêu cầu này.</li>
                                <li>Tất cả thông tin đối tượng hiệu chuẩn do khách hàng cung cấp và chịu hoàn toàn trách nhiệm.</li>
                                <li>Toàn bộ thông tin hiệu chuẩn sẽ được bảo mật theo quy định hiện hành của Phòng Dịch vụ và Công nghệ Hiệu chuẩn.</li>
                            </ul>
                        </div>

                        <!-- KHỐI KÝ NHẬN (BOTTOM RIGHT) -->
                        <div class="mt-4 flex justify-between items-end">
                            <div class="text-[8.5pt] italic text-gray-600">
                                Mã hợp đồng / Sales: <strong id="p-contract-sub" class="not-italic text-black font-bold">HĐ...</strong>
                            </div>

                            <div class="w-64 text-center">
                                <p class="text-[9pt] italic text-gray-800" id="p-date-place">
                                    Tp. HCM, ngày 29 tháng 10 năm 2026
                                </p>
                                <p class="text-[9.5pt] font-black uppercase mt-0.5 text-black">
                                    Người nhận yêu cầu
                                </p>
                                <p class="text-[8pt] italic text-gray-600 mb-1">
                                    (Ký và ghi rõ họ tên)
                                </p>

                                <!-- Chữ ký điện tử -->
                                <div class="h-16 flex items-center justify-center my-0.5">
                                    <img src="{sig_b64}" alt="Chữ ký Nguyễn Thị Thúy Bình" class="h-14 w-auto object-contain">
                                </div>

                                <p class="text-[10pt] font-black text-black uppercase tracking-wide">
                                    Nguyễn Thị Thúy Bình
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ============================================================== -->
            <!-- TAB 3: SỔ THEO DÕI NHẬN PTĐ VÀ TRẢ KẾT QUẢ                     -->
            <!-- ============================================================== -->
            <div id="tab-3-content" class="hidden space-y-6">
                <!-- Dashboard Statistics Cards -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    <div class="bg-white rounded-2xl p-4 shadow-xs border border-slate-200 flex items-center justify-between">
                        <div>
                            <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Tổng Phiếu Tiếp Nhận</span>
                            <div class="text-2xl font-black text-slate-900 mt-1" id="stat-total-count">0</div>
                            <span class="text-xs text-slate-400 font-medium">Bản ghi trong hệ thống</span>
                        </div>
                        <div class="w-12 h-12 rounded-2xl bg-blue-50 text-blue-600 flex items-center justify-center text-xl font-bold">
                            <i class="fa-solid fa-clipboard-list text-xl"></i>
                        </div>
                    </div>

                    <div class="bg-white rounded-2xl p-4 shadow-xs border border-slate-200 flex items-center justify-between">
                        <div>
                            <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Doanh Số (Chưa VAT)</span>
                            <div class="text-xl font-black text-digi mt-1" id="stat-total-revenue">0 VNĐ</div>
                            <span class="text-xs text-green-600 font-semibold">Doanh thu dự kiến</span>
                        </div>
                        <div class="w-12 h-12 rounded-2xl bg-red-50 text-digi flex items-center justify-center text-xl font-bold">
                            <i class="fa-solid fa-coins text-xl"></i>
                        </div>
                    </div>

                    <div class="bg-white rounded-2xl p-4 shadow-xs border border-slate-200 flex items-center justify-between">
                        <div>
                            <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Đã Xuất GCN</span>
                            <div class="text-2xl font-black text-emerald-600 mt-1" id="stat-cert-count">0</div>
                            <span class="text-xs text-slate-400 font-medium" id="stat-cert-percent">Tiến độ 0%</span>
                        </div>
                        <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-xl font-bold">
                            <i class="fa-solid fa-certificate text-xl"></i>
                        </div>
                    </div>

                    <div class="bg-white rounded-2xl p-4 shadow-xs border border-slate-200 flex items-center justify-between">
                        <div>
                            <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Đã Bàn Giao PTĐ</span>
                            <div class="text-2xl font-black text-purple-600 mt-1" id="stat-device-count">0</div>
                            <span class="text-xs text-slate-400 font-medium" id="stat-device-percent">Tiến độ 0%</span>
                        </div>
                        <div class="w-12 h-12 rounded-2xl bg-purple-50 text-purple-600 flex items-center justify-center text-xl font-bold">
                            <i class="fa-solid fa-truck-ramp-box text-xl"></i>
                        </div>
                    </div>
                </div>

                <!-- Filter & Action Toolbar -->
                <div class="bg-white rounded-2xl p-4 shadow-xs border border-slate-200 flex flex-wrap items-center justify-between gap-4">
                    <div class="flex flex-wrap items-center gap-3 flex-1 min-w-[280px]">
                        <!-- Live Search Input with FontAwesome Icon -->
                        <div class="relative flex-1 min-w-[220px]">
                            <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                                <i class="fa-solid fa-magnifying-glass"></i>
                            </span>
                            <input type="text" id="grid-search" oninput="debounceFilter()" placeholder="Tìm theo Mã phiếu, Khách hàng, Hợp đồng, KTV..."
                                class="w-full pl-10 pr-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40 focus:border-digi transition">
                        </div>

                        <!-- Status Filter -->
                        <select id="grid-filter-status" onchange="filterRecords()"
                            class="px-4 py-2.5 text-sm font-semibold bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-digi/40">
                            <option value="">Tất cả trạng thái</option>
                            <option value="cert_done">Đã Xuất GCN</option>
                            <option value="cert_pending">Chưa Xuất GCN</option>
                            <option value="device_done">Đã Giao PTĐ</option>
                            <option value="device_pending">Chưa Giao PTĐ</option>
                        </select>
                    </div>

                    <!-- Right Buttons: Excel Export & Add New -->
                    <div class="flex items-center space-x-2.5">
                        <button type="button" id="btn-export-excel" onclick="handleExportExcel()"
                            class="px-4 py-2.5 text-xs font-black text-emerald-800 bg-emerald-50 hover:bg-emerald-100 border border-emerald-300 rounded-xl transition flex items-center space-x-2">
                            <i class="fa-solid fa-file-excel text-emerald-700 text-sm"></i>
                            <span>XUẤT EXCEL (.XLSX)</span>
                        </button>

                        <button type="button" onclick="switchTab(1); resetForm();"
                            class="px-5 py-2.5 text-xs font-black text-white bg-gradient-to-r from-digi to-red-600 hover:from-digi-hover hover:to-red-700 rounded-xl shadow-xs transition flex items-center space-x-2">
                            <i class="fa-solid fa-plus"></i>
                            <span>Tiếp Nhận Phiếu Mới</span>
                        </button>
                    </div>
                </div>

                <!-- SỔ THEO DÕI: CUỘN DỌC/NGANG & GHIM CỐ ĐỊNH TIÊU ĐỀ -->
                <div class="bg-white rounded-2xl shadow-sm border border-slate-300 overflow-hidden">
                    <div class="overflow-x-auto overflow-y-auto max-h-[68vh] relative">
                        <table class="w-full text-left text-sm border-collapse">
                            <!-- Two-tier Header: Hạn chế màu sắc, ghim cố định, hiển thị đầy đủ 5 cột nhận/trả/hạn HC -->
                            <thead>
                                <tr class="sticky-header-row-1 text-slate-800 text-xs font-bold uppercase tracking-wider">
                                    <th rowspan="2" class="border border-slate-300 p-3 text-center w-12 bg-slate-200">STT</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 text-center w-28 bg-slate-200">Phiếu YC</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 min-w-[150px] bg-slate-200">Mã HĐ / Sales</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 min-w-[260px] bg-slate-200">Mô Tả Chi Tiết</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 min-w-[240px] bg-slate-200">Khách Hàng</th>
                                    <th colspan="4" class="border border-slate-300 p-2 text-center bg-slate-200 text-slate-800">Mã Mẫu</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 text-center w-14 bg-slate-200">SL</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 text-right min-w-[140px] bg-slate-200 text-slate-900">Doanh Số (VNĐ)</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 min-w-[130px] bg-slate-200">NVHC</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 min-w-[140px] bg-slate-200">Người nhận PTĐ</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 text-center min-w-[130px] bg-slate-200">Ngày nhận PTĐ</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 min-w-[140px] bg-slate-200">Người trả PTĐ</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 text-center min-w-[130px] bg-slate-200">Ngày trả PTĐ</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 text-center min-w-[140px] bg-slate-200">Ngày hiệu chuẩn tiếp theo</th>
                                    <th rowspan="2" class="border border-slate-300 p-2 text-center w-24 bg-slate-200 text-slate-800">Đã Xuất GCN</th>
                                    <th rowspan="2" class="border border-slate-300 p-2 text-center w-24 bg-slate-200 text-slate-800">Đã Giao PTĐ</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 min-w-[160px] bg-slate-200">Ghi Chú</th>
                                    <th rowspan="2" class="border border-slate-300 p-3 text-center w-28 bg-slate-200" id="th-actions">Thao Tác</th>
                                </tr>
                                <tr class="sticky-header-row-2 text-slate-700 text-[11px] font-bold uppercase">
                                    <th class="border border-slate-300 p-2 text-center w-24 bg-slate-100">Nhiệt</th>
                                    <th class="border border-slate-300 p-2 text-center w-24 bg-slate-100">Nhiệt ẩm</th>
                                    <th class="border border-slate-300 p-2 text-center w-24 bg-slate-100">Áp</th>
                                    <th class="border border-slate-300 p-2 text-center w-24 bg-slate-100">Khí</th>
                                </tr>
                            </thead>
                            <tbody id="grid-tbody" class="divide-y divide-slate-200 bg-white">
                                <!-- Populated dynamically -->
                            </tbody>
                        </table>
                    </div>

                    <!-- Grid Empty State -->
                    <div id="grid-empty" class="hidden p-10 text-center text-slate-400">
                        <i class="fa-solid fa-folder-open text-4xl mb-3 text-slate-300"></i>
                        <p class="font-bold text-base text-slate-600">Không tìm thấy bản ghi nào phù hợp</p>
                        <p class="text-xs text-slate-400 mt-1">Hãy thử đổi từ khóa tìm kiếm hoặc lọc lại trạng thái</p>
                    </div>
                </div>
            </div>
        </main>
    </div>

    <!-- ============================================================== -->
    <!-- MODAL CHỈNH SỬA BẢN GHI (DÀNH CHO ADMIN)                       -->
    <!-- ============================================================== -->
    <div id="edit-modal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs">
        <div class="bg-white rounded-3xl w-full max-w-2xl max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-200 p-7 relative">
            <div class="flex items-center justify-between border-b border-slate-200 pb-3.5 mb-5">
                <div class="flex items-center space-x-3">
                    <span class="p-2.5 rounded-2xl bg-red-100 text-digi text-base"><i class="fa-solid fa-pen-to-square"></i></span>
                    <div>
                        <h3 class="text-lg font-black text-slate-900">Chỉnh Sửa Sổ Theo Dõi PTĐ</h3>
                        <p class="text-xs text-slate-500 font-medium" id="edit-modal-code">Phiếu: HC.26.xxx</p>
                    </div>
                </div>
                <button type="button" onclick="closeEditModal()" class="text-slate-400 hover:text-slate-700 p-2 rounded-xl text-lg">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <form id="edit-form" onsubmit="handleSaveEdit(event)" class="space-y-4 text-xs">
                <input type="hidden" id="edit-id">

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Mã HĐ / Sales Phụ Trách</label>
                        <input type="text" id="edit-contract" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl">
                    </div>

                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Khách Hàng</label>
                        <input type="text" id="edit-customer" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl font-bold">
                    </div>

                    <div class="md:col-span-2">
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Mô Tả Chi Tiết Dịch Vụ</label>
                        <textarea id="edit-desc" rows="2" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl"></textarea>
                    </div>

                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Mã mẫu Nhiệt (1 mã/dòng)</label>
                        <textarea id="edit-code-temp" rows="2" class="w-full px-3 py-2 border border-slate-300 rounded-xl font-mono text-xs leading-relaxed resize-y"></textarea>
                    </div>
                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Mã mẫu Nhiệt ẩm (1 mã/dòng)</label>
                        <textarea id="edit-code-hum" rows="2" class="w-full px-3 py-2 border border-slate-300 rounded-xl font-mono text-xs leading-relaxed resize-y"></textarea>
                    </div>
                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Mã mẫu Áp (1 mã/dòng)</label>
                        <textarea id="edit-code-press" rows="2" class="w-full px-3 py-2 border border-slate-300 rounded-xl font-mono text-xs leading-relaxed resize-y"></textarea>
                    </div>
                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Mã mẫu Khí (1 mã/dòng)</label>
                        <textarea id="edit-code-gas" rows="2" class="w-full px-3 py-2 border border-slate-300 rounded-xl font-mono text-xs leading-relaxed resize-y"></textarea>
                    </div>

                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Doanh Số (Chưa VAT) (VNĐ)</label>
                        <input type="number" id="edit-revenue" step="50000" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl font-black text-digi">
                    </div>

                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Nhân Viên Hiệu Chuẩn (NVHC)</label>
                        <input type="text" id="edit-technician" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl font-medium">
                    </div>

                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Người Nhận PTĐ</label>
                        <input type="text" id="edit-received-person" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl font-medium" placeholder="Ví dụ: Mr. Lộc, Ms. Bình...">
                    </div>

                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Ngày Nhận PTĐ</label>
                        <input type="text" id="edit-received-date" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl" placeholder="DD/MM/YYYY">
                    </div>

                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Người Trả PTĐ</label>
                        <input type="text" id="edit-returned-person" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl font-medium" placeholder="Ví dụ: Mr. Tú, Mr. Lộc...">
                    </div>

                    <div>
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Ngày Trả PTĐ</label>
                        <input type="text" id="edit-returned-date" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl" placeholder="DD/MM/YYYY">
                    </div>

                    <div class="md:col-span-2">
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Ngày Hiệu Chuẩn Tiếp Theo</label>
                        <input type="text" id="edit-next-cal-date" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl font-medium" placeholder="DD/MM/YYYY (Ví dụ: 25/01/2027)">
                    </div>

                    <div class="flex items-center space-x-6 pt-3 md:col-span-2">
                        <label class="flex items-center space-x-2 cursor-pointer font-bold text-emerald-800">
                            <input type="checkbox" id="edit-cert-done" class="rounded text-emerald-600 focus:ring-emerald-500 h-5 w-5">
                            <span>Đã Xuất GCN</span>
                        </label>
                        <label class="flex items-center space-x-2 cursor-pointer font-bold text-purple-800">
                            <input type="checkbox" id="edit-device-done" class="rounded text-purple-600 focus:ring-purple-500 h-5 w-5">
                            <span>Đã Giao PTĐ</span>
                        </label>
                    </div>

                    <div class="md:col-span-2">
                        <label class="block font-bold text-slate-700 mb-1.5 uppercase text-xs">Ghi Chú</label>
                        <input type="text" id="edit-note" class="w-full px-3.5 py-2.5 border border-slate-300 rounded-xl">
                    </div>
                </div>

                <div class="pt-5 border-t border-slate-200 flex justify-end space-x-3">
                    <button type="button" onclick="closeEditModal()" class="px-5 py-2.5 font-bold text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-xl text-sm">
                        Hủy
                    </button>
                    <button type="submit" class="px-6 py-2.5 font-extrabold text-white bg-digi hover:bg-digi-hover rounded-xl shadow-md text-sm">
                        Lưu Thay Đổi
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- TOAST NOTIFICATIONS -->
    <div id="toast-container" class="fixed bottom-4 right-4 z-50 space-y-2 pointer-events-none"></div>

    <!-- ============================================================== -->
    <!-- JAVASCRIPT APPLICATION LOGIC                                   -->
    <!-- ============================================================== -->
    <script>
        // APPLICATION STATE
        let currentUser = null;
        let allRequests = [];
        let currentViewingRequest = null;
        let filterDebounceTimer = null;

        // Pricing Rules
        const PRICE_TEMP = 500000;
        const PRICE_PRESS = 500000;
        const PRICE_HUM = 750000;
        const PRICE_GAS = 1500000;

        // ----------------- INITIALIZATION -----------------
        window.addEventListener('DOMContentLoaded', async () => {{
            initDefaultDeviceRow();

            // Kiểm tra session
            const savedUser = localStorage.getItem('digi_cal_user');
            if (savedUser) {{
                try {{
                    currentUser = JSON.parse(savedUser);
                    applyUserPermissions();
                    hideAuthModal();
                }} catch (e) {{
                    showAuthModal();
                }}
            }} else {{
                showAuthModal();
            }}

            await loadRequestsData();
            await fetchNextCode();
        }});

        // ----------------- AUTH (BẢO MẬT & ĐIỀN THÔ) -----------------
        function showAuthModal() {{
            document.getElementById('auth-modal').classList.remove('hidden');
            document.getElementById('login-email').value = '';
            document.getElementById('login-password').value = '';
        }}

        function hideAuthModal() {{
            document.getElementById('auth-modal').classList.add('hidden');
        }}

        function togglePasswordVisibility() {{
            const pwd = document.getElementById('login-password');
            const icon = document.getElementById('eye-icon');
            if (pwd.type === 'password') {{
                pwd.type = 'text';
                icon.className = 'fa-solid fa-eye-slash text-sm';
            }} else {{
                pwd.type = 'password';
                icon.className = 'fa-solid fa-eye text-sm';
            }}
        }}

        async function handleLogin(e) {{
            e.preventDefault();
            const email = document.getElementById('login-email').value.trim();
            const password = document.getElementById('login-password').value.trim();
            const errDiv = document.getElementById('login-error');
            const submitBtn = document.getElementById('btn-login-submit');

            errDiv.classList.add('hidden');
            if (!email || !password) {{
                errDiv.textContent = 'Vui lòng nhập đầy đủ Email và Mật khẩu!';
                errDiv.classList.remove('hidden');
                return;
            }}

            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin mr-2"></i>Đang kiểm tra...';

            try {{
                const res = await fetch('/api/auth/login', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ email, password }})
                }});
                const data = await res.json();

                if (res.ok && data.success) {{
                    currentUser = data.user;
                    localStorage.setItem('digi_cal_user', JSON.stringify(currentUser));
                    applyUserPermissions();
                    hideAuthModal();
                    showToast('Đăng nhập thành công! Chào mừng ' + currentUser.name, 'success');
                    await loadRequestsData();
                }} else {{
                    validateLocalCredentials(email, password);
                }}
            }} catch (err) {{
                validateLocalCredentials(email, password);
            }} finally {{
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<i class="fa-solid fa-arrow-right-to-bracket text-base"></i><span>Xác Thực & Đăng Nhập</span>';
            }}
        }}

        function validateLocalCredentials(email, password) {{
            const errDiv = document.getElementById('login-error');
            if (email.toLowerCase() === 'cst@digivn.com' && password === 'CST@654') {{
                currentUser = {{
                    email: 'CST@digivn.com',
                    name: 'Quản trị viên CST',
                    role: 'admin'
                }};
            }} else if (email.toLowerCase() === 'nhanvien@digivn.com' && password === '123456') {{
                currentUser = {{
                    email: 'nhanvien@digivn.com',
                    name: 'Nhân viên Tiếp nhận',
                    role: 'user'
                }};
            }} else {{
                errDiv.textContent = 'Email hoặc mật khẩu không chính xác. Chỉ người có quyền mới được đăng nhập!';
                errDiv.classList.remove('hidden');
                return;
            }}

            localStorage.setItem('digi_cal_user', JSON.stringify(currentUser));
            applyUserPermissions();
            hideAuthModal();
            showToast('Đăng nhập thành công! Quyền: ' + (currentUser.role === 'admin' ? 'Quản trị CST' : 'Nhân viên'), 'success');
            loadRequestsData();
        }}

        function applyUserPermissions() {{
            if (!currentUser) return;

            document.getElementById('current-user-name').textContent = currentUser.name;
            document.getElementById('current-user-email').textContent = currentUser.email;

            const badge = document.getElementById('current-role-badge');
            const btnExport = document.getElementById('btn-export-excel');

            if (currentUser.role === 'admin') {{
                badge.textContent = 'ADMIN';
                badge.className = 'inline-flex items-center px-2 py-0.5 rounded-md text-[11px] font-black bg-red-100 text-digi uppercase';
                if (btnExport) btnExport.classList.remove('opacity-50', 'cursor-not-allowed');
            }} else {{
                badge.textContent = 'NHÂN VIÊN';
                badge.className = 'inline-flex items-center px-2 py-0.5 rounded-md text-[11px] font-black bg-blue-100 text-blue-700 uppercase';
            }}

            renderGrid();
        }}

        async function handleLogout() {{
            try {{
                await fetch('/api/auth/logout', {{ method: 'POST' }});
            }} catch (e) {{}}
            localStorage.removeItem('digi_cal_user');
            currentUser = null;
            showAuthModal();
            showToast('Đã đăng xuất khỏi phiên làm việc', 'info');
        }}

        // ----------------- TABS NAVIGATION -----------------
        function switchTab(tabIndex) {{
            [1, 2, 3].forEach(idx => {{
                const content = document.getElementById(`tab-${{idx}}-content`);
                const btn = document.getElementById(`nav-tab-${{idx}}`);
                if (idx === tabIndex) {{
                    content.classList.remove('hidden');
                    btn.className = 'px-5 py-2.5 rounded-xl text-sm font-extrabold transition flex items-center space-x-2 bg-white text-digi shadow-xs';
                }} else {{
                    content.classList.add('hidden');
                    btn.className = 'px-5 py-2.5 rounded-xl text-sm font-extrabold transition flex items-center space-x-2 text-slate-600 hover:text-slate-900';
                }}
            }});

            if (tabIndex === 2 && currentViewingRequest) {{
                renderPrintSheet(currentViewingRequest);
            }} else if (tabIndex === 3) {{
                renderGrid();
            }}
        }}

        // ----------------- TAB 1: FORM & CALCULATION LOGIC -----------------
        function initDefaultDeviceRow() {{
            const tbody = document.getElementById('device-tbody');
            tbody.innerHTML = '';
            addDeviceRow('Testo 350', 'Tiêu chuẩn', 1, 'Bình thường, đầy đủ phụ kiện');
        }}

        function addDeviceRow(name = '', specs = 'Tiêu chuẩn', qty = 1, condition = 'Bình thường') {{
            const tbody = document.getElementById('device-tbody');
            const rowCount = tbody.children.length + 1;
            const tr = document.createElement('tr');
            tr.className = 'device-row';
            tr.innerHTML = `
                <td class="p-2.5 text-center font-bold text-slate-500">${{rowCount}}</td>
                <td class="p-2.5">
                    <input type="text" name="dev_name" value="${{name}}" required placeholder="Tên thiết bị..." oninput="calculateEverything()"
                        class="w-full px-3 py-1.5 border border-slate-200 rounded-lg focus:ring-1 focus:ring-digi font-bold text-slate-900">
                </td>
                <td class="p-2.5">
                    <input type="text" name="dev_specs" value="${{specs}}" placeholder="Tiêu chuẩn"
                        class="w-full px-3 py-1.5 border border-slate-200 rounded-lg focus:ring-1 focus:ring-digi">
                </td>
                <td class="p-2.5">
                    <input type="number" name="dev_qty" min="1" value="${{qty}}" oninput="calculateEverything()"
                        class="w-full px-3 py-1.5 border border-slate-200 rounded-lg text-center font-bold focus:ring-1 focus:ring-digi">
                </td>
                <td class="p-2.5">
                    <input type="text" name="dev_condition" value="${{condition}}" placeholder="Tình trạng nhận..."
                        class="w-full px-3 py-1.5 border border-slate-200 rounded-lg focus:ring-1 focus:ring-digi">
                </td>
                <td class="p-2.5 text-center">
                    <button type="button" onclick="removeDeviceRow(this)" title="Xóa dòng"
                        class="text-red-400 hover:text-red-600 p-1.5 transition">
                        <i class="fa-solid fa-trash-can"></i>
                    </button>
                </td>
            `;
            tbody.appendChild(tr);
            calculateEverything();
        }}

        function removeDeviceRow(btn) {{
            const tbody = document.getElementById('device-tbody');
            if (tbody.children.length <= 1) {{
                showToast('Phải có ít nhất 1 thiết bị trong phiếu!', 'warning');
                return;
            }}
            btn.closest('tr').remove();
            Array.from(tbody.children).forEach((tr, i) => {{
                tr.children[0].textContent = i + 1;
            }});
            calculateEverything();
        }}

        function selectAllGases(select = true) {{
            const checkboxes = document.querySelectorAll('input[name="gas_param"]');
            checkboxes.forEach(cb => cb.checked = select);
            calculateEverything();
        }}

        function calculateEverything() {{
            const selectedGases = [];
            document.querySelectorAll('input[name="gas_param"]:checked').forEach(cb => {{
                selectedGases.push(cb.value);
            }});

            const hasTemp = document.getElementById('param-temp').checked;
            const hasPress = document.getElementById('param-press').checked;
            const hasHum = document.getElementById('param-hum').checked;

            let totalQty = 0;
            let firstDeviceName = 'Thiết bị';
            const devRows = document.querySelectorAll('#device-tbody tr');
            devRows.forEach((tr, idx) => {{
                const nameInput = tr.querySelector('input[name="dev_name"]');
                const qtyInput = tr.querySelector('input[name="dev_qty"]');
                const q = parseInt(qtyInput ? qtyInput.value : 1) || 1;
                totalQty += q;
                if (idx === 0 && nameInput && nameInput.value.trim()) {{
                    firstDeviceName = nameInput.value.trim();
                }}
            }});
            if (totalQty === 0) totalQty = 1;

            const gasCost = selectedGases.length * PRICE_GAS;
            const tempCost = hasTemp ? PRICE_TEMP : 0;
            const pressCost = hasPress ? PRICE_PRESS : 0;
            const humCost = hasHum ? (PRICE_HUM * totalQty) : 0;

            const totalRevenue = gasCost + tempCost + pressCost + humCost;

            document.getElementById('revenue-display').textContent = formatCurrency(totalRevenue);
            document.getElementById('calculated-revenue').value = totalRevenue;

            const formulaParts = [];
            if (selectedGases.length > 0) {{
                formulaParts.push(`${{selectedGases.length}} khí (${{formatCurrency(gasCost)}})`);
            }}
            if (hasTemp) {{
                formulaParts.push(`Nhiệt độ (500.000 VNĐ)`);
            }}
            if (hasPress) {{
                formulaParts.push(`Chênh áp (500.000 VNĐ)`);
            }}
            if (hasHum) {{
                formulaParts.push(`Nhiệt ẩm (${{formatCurrency(humCost)}})`);
            }}

            const formulaEl = document.getElementById('revenue-formula');
            if (formulaParts.length > 0) {{
                formulaEl.textContent = 'Công thức: ' + formulaParts.join(' + ');
            }} else {{
                formulaEl.textContent = 'Chưa chọn thông số hiệu chuẩn';
            }}

            let generatedDesc = '';
            if (selectedGases.length > 0 || hasTemp || hasPress || hasHum) {{
                const descParams = [];
                if (selectedGases.length > 0) {{
                    descParams.push(selectedGases.join(', '));
                }}
                if (hasTemp) descParams.push('NHIỆT ĐỘ');
                if (hasPress) descParams.push('CHÊNH ÁP');
                if (hasHum) descParams.push('NHIỆT ẨM');

                generatedDesc = `Dịch vụ hiệu chuẩn ${{firstDeviceName}} tại các thông số: ${{descParams.join('; ')}}`;
            }} else {{
                generatedDesc = `Dịch vụ hiệu chuẩn ${{firstDeviceName}}`;
            }}

            document.getElementById('service-description').value = generatedDesc;
            autoSyncProcedures(hasTemp, hasHum, hasPress, selectedGases.length > 0);
            autoAllocateSampleCodes(false);
        }}

        function autoSyncProcedures(hasTemp, hasHum, hasPress, hasGas) {{
            const procCbs = document.querySelectorAll('input[name="procedure"]');
            procCbs.forEach(cb => {{
                const val = cb.value;
                if (val.includes('012023') && hasTemp) cb.checked = true;
                if (val.includes('022023') && hasHum) cb.checked = true;
                if (val.includes('032023') && hasPress) cb.checked = true;
                if (val.includes('042023') && hasGas) cb.checked = true;
            }});
        }}

        function getCodePrefixAndStt() {{
            const codeInput = document.getElementById('req-code');
            const code = codeInput ? codeInput.value.trim() : '';
            const parts = code.split('.');
            let nam = new Date().getFullYear().toString().slice(-2);
            let stt_goc = 1;
            if (parts.length >= 3) {{
                nam = parts[1];
                stt_goc = parseInt(parts[2], 10) || 1;
            }}
            return {{ nam, stt_goc }};
        }}

        function autoAllocateSampleCodes(manualClick = false) {{
            const {{ nam, stt_goc }} = getCodePrefixAndStt();

            let totalQty = 0;
            document.querySelectorAll('#device-tbody tr').forEach(tr => {{
                const qtyInput = tr.querySelector('input[name="dev_qty"]');
                const q = parseInt(qtyInput ? qtyInput.value : 1, 10) || 1;
                totalQty += q;
            }});
            if (totalQty < 1) totalQty = 1;

            const hasTemp = document.getElementById('param-temp').checked;
            const hasHum = document.getElementById('param-hum').checked;
            const hasPress = document.getElementById('param-press').checked;
            const hasGas = document.querySelectorAll('input[name="gas_param"]:checked').length > 0;

            function generateGroupCodes(nhom, count) {{
                const arr = [];
                for (let i = 1; i <= count; i++) {{
                    const stt = String(stt_goc + i - 1).padStart(3, '0');
                    arr.push(`HC.${{nhom}}.${{nam}}.${{stt}}`);
                }}
                return arr.join('\n');
            }}

            const tempEl = document.getElementById('code-temp');
            const humEl = document.getElementById('code-hum');
            const pressEl = document.getElementById('code-press');
            const gasEl = document.getElementById('code-gas');

            if (!tempEl) return;

            const autoRows = Math.max(2, Math.min(8, totalQty));

            if (hasTemp) {{
                tempEl.value = generateGroupCodes(1, totalQty);
            }} else if (!manualClick) {{
                tempEl.value = '';
            }}
            tempEl.rows = autoRows;

            if (hasHum) {{
                humEl.value = generateGroupCodes(2, totalQty);
            }} else if (!manualClick) {{
                humEl.value = '';
            }}
            humEl.rows = autoRows;

            if (hasPress) {{
                pressEl.value = generateGroupCodes(3, totalQty);
            }} else if (!manualClick) {{
                pressEl.value = '';
            }}
            pressEl.rows = autoRows;

            if (hasGas) {{
                gasEl.value = generateGroupCodes(4, totalQty);
            }} else if (!manualClick) {{
                gasEl.value = '';
            }}
            gasEl.rows = autoRows;

            // Nếu người dùng bấm nút thủ công nhưng chưa tick thông số nào: sinh theo mặc định
            if (manualClick && !hasTemp && !hasHum && !hasPress && !hasGas) {{
                tempEl.value = generateGroupCodes(1, totalQty);
                humEl.value = generateGroupCodes(2, totalQty);
                pressEl.value = generateGroupCodes(3, totalQty);
                gasEl.value = generateGroupCodes(4, totalQty);
            }}

            updateSampleCodeBadges();

            if (manualClick) {{
                showToast(`Đã tự động phân bổ mã mẫu cho số lượng: ${{totalQty}} (mỗi mã 1 dòng)!`, 'success');
            }}
        }}

        function updateSampleCodeBadges() {{
            ['temp', 'hum', 'press', 'gas'].forEach(grp => {{
                const el = document.getElementById(`code-${{grp}}`);
                const badge = document.getElementById(`badge-count-${{grp}}`);
                if (el && badge) {{
                    const count = el.value.split('\n').map(s => s.trim()).filter(Boolean).length;
                    badge.textContent = `${{count}} mã`;
                    if (count > 0) {{
                        badge.className = 'text-[11px] font-mono font-bold text-digi bg-red-50 border border-red-200 px-2 py-0.5 rounded-md';
                    }} else {{
                        badge.className = 'text-[11px] font-mono font-medium text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md';
                    }}
                }}
            }});
        }}

        function formatSampleCodeCell(codeStr) {{
            if (!codeStr || !codeStr.trim()) return '<span class="text-slate-300">—</span>';
            const items = codeStr.split(/[\r\n,;]+|<br\\s*\\/?>/i)
                .map(s => s.trim())
                .filter(Boolean);
            if (items.length === 0) return '<span class="text-slate-300">—</span>';
            return items.map(c => `<div class="sample-code-item font-mono text-xs font-bold text-slate-800 py-0.5 whitespace-nowrap leading-tight">${{c}}</div>`).join('');
        }}

        function formatToLines(str) {{
            if (!str) return '';
            return str.split(/[\r\n,;]+|<br\\s*\\/?>/i).map(s => s.trim()).filter(Boolean).join('\n');
        }}

        function getCleanSampleCodes(elementId) {{
            const el = document.getElementById(elementId);
            if (!el) return '';
            return el.value.split('\n').map(s => s.trim()).filter(Boolean).join('\n');
        }}

        async function fetchNextCode() {{
            try {{
                const res = await fetch('/api/requests/next-code');
                if (res.ok) {{
                    const data = await res.json();
                    document.getElementById('req-code').value = data.next_code;
                    document.getElementById('form-code-badge').textContent = data.next_code;
                    autoAllocateSampleCodes(false);
                    return;
                }}
            }} catch (e) {{}}

            const yy = new Date().getFullYear().toString().slice(-2);
            let maxNum = 0;
            allRequests.forEach(r => {{
                const parts = (r.code || '').split('.');
                if (parts.length === 3 && !isNaN(parts[2])) {{
                    maxNum = Math.max(maxNum, parseInt(parts[2]));
                }}
            }});
            const nextCode = `HC.${{yy}}.${{String(maxNum + 1).padStart(3, '0')}}`;
            document.getElementById('req-code').value = nextCode;
            document.getElementById('form-code-badge').textContent = nextCode;
        }}

        function resetForm() {{
            document.getElementById('calibration-form').reset();
            initDefaultDeviceRow();
            fetchNextCode();
            calculateEverything();
            showToast('Đã làm mới form nhập liệu!', 'info');
        }}

        async function submitCalibrationForm(stayOnTab = false) {{
            const code = document.getElementById('req-code').value.trim();
            const customerName = document.getElementById('req-customer-name').value.trim();

            if (!code || !customerName) {{
                showToast('Vui lòng nhập Mã phiếu và Tên khách hàng!', 'warning');
                return;
            }}

            const devices = [];
            document.querySelectorAll('#device-tbody tr').forEach((tr, i) => {{
                devices.push({{
                    stt: i + 1,
                    name: tr.querySelector('input[name="dev_name"]').value.trim(),
                    specs: tr.querySelector('input[name="dev_specs"]').value.trim(),
                    qty: parseInt(tr.querySelector('input[name="dev_qty"]').value) || 1,
                    condition: tr.querySelector('input[name="dev_condition"]').value.trim()
                }});
            }});

            const procedures = [];
            document.querySelectorAll('input[name="procedure"]:checked').forEach(cb => {{
                procedures.push(cb.value);
            }});

            const paramsGas = [];
            document.querySelectorAll('input[name="gas_param"]:checked').forEach(cb => {{
                paramsGas.push(cb.value);
            }});

            const paramsMeasure = [];
            if (document.getElementById('param-temp').checked) paramsMeasure.push('NHIET_DO');
            if (document.getElementById('param-press').checked) paramsMeasure.push('CHENH_AP');
            if (document.getElementById('param-hum').checked) paramsMeasure.push('NHIET_AM');

            const payload = {{
                code: code,
                contract_sales: document.getElementById('req-contract').value.trim(),
                customer_name: customerName,
                customer_address: document.getElementById('req-customer-address').value.trim(),
                customer_tax_code: document.getElementById('req-tax-code').value.trim(),
                contact_person: document.getElementById('req-contact-person').value.trim(),
                contact_phone: document.getElementById('req-contact-phone').value.trim(),
                contact_email: document.getElementById('req-contact-email').value.trim(),
                devices: devices,
                code_temp: getCleanSampleCodes('code-temp'),
                code_hum: getCleanSampleCodes('code-hum'),
                code_press: getCleanSampleCodes('code-press'),
                code_gas: getCleanSampleCodes('code-gas'),
                procedures: procedures,
                params_gas: paramsGas,
                params_measure: paramsMeasure,
                service_desc: document.getElementById('service-description').value.trim(),
                revenue: parseFloat(document.getElementById('calculated-revenue').value) || 0,
                req_adjust: document.getElementById('req-adjust').checked,
                req_uncertainty: document.getElementById('req-uncertainty').checked,
                req_compliance: document.getElementById('req-compliance').checked,
                req_next_date: document.getElementById('req-next-date').checked,
                return_method: document.querySelector('input[name="return_method"]:checked')?.value || 'CHUYEN_PHAT',
                expected_return_date: document.getElementById('req-expected-return').value,
                received_date: document.getElementById('req-received-date').value.trim(),
                received_person: document.getElementById('req-recipient-person').value.trim(),
                returned_date: document.getElementById('req-expected-return').value,
                returned_person: document.getElementById('req-handover-person').value.trim(),
                technician: document.getElementById('req-technician').value.trim() || 'Nguyễn Minh Tú',
                handover_person: document.getElementById('req-handover-person').value.trim(),
                recipient_person: document.getElementById('req-recipient-person').value.trim(),
                next_cal_date: '',
                cert_done: 0,
                device_done: 0,
                accessories_note: document.getElementById('req-accessories').value.trim(),
                general_note: document.getElementById('req-notes').value.trim()
            }};

            try {{
                const res = await fetch('/api/requests', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify(payload)
                }});
                const result = await res.json();

                if (res.ok && result.success) {{
                    showToast('Đã lưu thành công Phiếu ' + code + ' vào Sổ theo dõi!', 'success');
                    await loadRequestsData();
                    currentViewingRequest = allRequests.find(r => r.code === code) || payload;

                    if (!stayOnTab) {{
                        switchTab(2);
                        renderPrintSheet(currentViewingRequest);
                    }}
                }} else {{
                    showToast(result.error || 'Lỗi khi lưu phiếu', 'error');
                }}
            }} catch (err) {{
                payload.id = Date.now();
                allRequests.unshift(payload);
                localStorage.setItem('digi_cal_requests', JSON.stringify(allRequests));
                showToast('Đã lưu cục bộ Phiếu ' + code + ' thành công!', 'success');
                renderGrid();
                currentViewingRequest = payload;
                if (!stayOnTab) {{
                    switchTab(2);
                    renderPrintSheet(payload);
                }}
            }}
        }}

        // ----------------- TAB 2: RENDER BM.6.2.5 PRINT SHEET (NGAY HÀNG) -----------------
        function renderPrintSheet(req) {{
            if (!req) return;
            currentViewingRequest = req;

            document.getElementById('p-form-code-title').textContent = `Số: ${{req.code}}`;
            document.getElementById('print-code-indicator').textContent = req.code;
            document.getElementById('p-customer-name').textContent = req.customer_name || 'N/A';
            document.getElementById('p-customer-address').textContent = req.customer_address || 'Việt Nam';
            document.getElementById('p-customer-tax').textContent = req.customer_tax_code || 'N/A';
            document.getElementById('p-contact-person').textContent = req.contact_person || 'N/A';
            document.getElementById('p-contact-phone').textContent = req.contact_phone || 'N/A';
            document.getElementById('p-contact-email').textContent = req.contact_email || 'N/A';

            // Bảng thiết bị
            const tbody = document.getElementById('p-devices-tbody');
            tbody.innerHTML = '';
            const devs = req.devices || [];
            if (devs.length === 0) {{
                tbody.innerHTML = '<tr><td colspan="5" class="border border-black p-2 text-center">Chưa có thông tin thiết bị</td></tr>';
            }} else {{
                devs.forEach((d, idx) => {{
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td class="border border-black p-1.5 text-center font-bold">${{idx + 1}}</td>
                        <td class="border border-black p-1.5 font-bold">${{d.name || ''}}</td>
                        <td class="border border-black p-1.5 text-center">${{d.specs || 'Tiêu chuẩn'}}</td>
                        <td class="border border-black p-1.5 text-center font-bold">${{d.qty || 1}}</td>
                        <td class="border border-black p-1.5">${{d.condition || 'Bình thường'}}</td>
                    `;
                    tbody.appendChild(tr);
                }});
            }}

            // Quy trình
            const pList = document.getElementById('p-procedures-list');
            const procs = req.procedures || [];
            if (procs.length > 0) {{
                pList.innerHTML = procs.filter(Boolean).map(p => `• ${{p}}`).join('<br>');
            }} else {{
                pList.innerHTML = '• DIGI.QT.HC.012023 QTHC Nhiệt kế chỉ thị hiện số và tương tự';
            }}

            document.getElementById('p-service-desc').textContent = req.service_desc || 'Dịch vụ hiệu chuẩn thiết bị đo';

            renderCheckItem('p-req-adjust', req.req_adjust, 'Hiệu chuẩn có hiệu chỉnh');
            renderCheckItem('p-req-uncertainty', req.req_uncertainty ?? true, 'Công bố độ không đảm bảo đo');
            renderCheckItem('p-req-compliance', req.req_compliance, 'Tuyên bố sự phù hợp');
            renderCheckItem('p-req-next-date', req.req_next_date ?? true, 'Ghi ngày đề nghị hiệu chuẩn tiếp theo');

            const returnMethodEl = document.getElementById('p-return-method');
            if (req.return_method === 'VP') {{
                returnMethodEl.innerHTML = '<span class="font-bold">[x] Trả trực tiếp tại văn phòng hiệu chuẩn</span><span>[ ] Gửi chuyển phát</span>';
            }} else {{
                returnMethodEl.innerHTML = '<span>[ ] Trả trực tiếp tại văn phòng hiệu chuẩn</span><span class="font-bold">[x] Gửi chuyển phát</span>';
            }}

            document.getElementById('p-expected-date').textContent = req.expected_return_date ? formatDateVN(req.expected_return_date) : 'Theo thỏa thuận';
            document.getElementById('p-cost').textContent = formatCurrency(req.revenue || 0);
            document.getElementById('p-accessories').textContent = req.accessories_note || 'Cáp nguồn, đầu đo theo máy';
            document.getElementById('p-general-note').textContent = req.general_note || 'Không có';
            document.getElementById('p-contract-sub').textContent = req.contract_sales || req.code;

            const today = new Date();
            document.getElementById('p-date-place').textContent = `Tp. HCM, ngày ${{today.getDate()}} tháng ${{today.getMonth() + 1}} năm ${{today.getFullYear()}}`;
        }}

        function renderCheckItem(elementId, isChecked, text) {{
            const el = document.getElementById(elementId);
            if (isChecked) {{
                el.innerHTML = `<span class="font-mono font-bold text-black">[x]</span><span class="font-bold">${{text}}</span>`;
            }} else {{
                el.innerHTML = `<span class="font-mono text-gray-500">[ ]</span><span>${{text}}</span>`;
            }}
        }}

        function loadRequestToPrint(idOrCode) {{
            const req = allRequests.find(r => r.id == idOrCode || r.code == idOrCode);
            if (req) {{
                renderPrintSheet(req);
            }}
        }}

        // ----------------- TAB 3: ISO DATA GRID & CRUD -----------------
        async function loadRequestsData() {{
            try {{
                const res = await fetch('/api/requests');
                if (res.ok) {{
                    const result = await res.json();
                    allRequests = result.data || [];
                    updateDashboardStats(result.summary);
                    renderGrid();
                    populatePrintSelector();
                    return;
                }}
            }} catch (e) {{}}

            const localData = localStorage.getItem('digi_cal_requests');
            if (localData) {{
                allRequests = JSON.parse(localData);
            }}
            updateDashboardStats();
            renderGrid();
            populatePrintSelector();
        }}

        function updateDashboardStats(summary = null) {{
            let count = allRequests.length;
            let revenue = 0;
            let certCount = 0;
            let deviceCount = 0;

            if (summary) {{
                count = summary.total_count;
                revenue = summary.total_revenue;
                certCount = summary.cert_count;
                deviceCount = summary.device_count;
            }} else {{
                allRequests.forEach(r => {{
                    revenue += (r.revenue || 0);
                    if (r.cert_done) certCount++;
                    if (r.device_done) deviceCount++;
                }});
            }}

            document.getElementById('stat-total-count').textContent = count;
            document.getElementById('stat-total-revenue').textContent = formatCurrency(revenue);
            document.getElementById('stat-cert-count').textContent = `${{certCount}} / ${{count}}`;
            document.getElementById('stat-device-count').textContent = `${{deviceCount}} / ${{count}}`;

            const certPct = count > 0 ? Math.round((certCount / count) * 100) : 0;
            const devPct = count > 0 ? Math.round((deviceCount / count) * 100) : 0;
            document.getElementById('stat-cert-percent').textContent = `Tiến độ ${{certPct}}%`;
            document.getElementById('stat-device-percent').textContent = `Tiến độ ${{devPct}}%`;
        }}

        function populatePrintSelector() {{
            const sel = document.getElementById('print-selector');
            sel.innerHTML = '';
            allRequests.forEach(r => {{
                const opt = document.createElement('option');
                opt.value = r.id;
                opt.textContent = `${{r.code}} - ${{r.customer_name ? r.customer_name.slice(0, 32) + '...' : ''}}`;
                sel.appendChild(opt);
            }});

            if (allRequests.length > 0 && !currentViewingRequest) {{
                currentViewingRequest = allRequests[0];
                renderPrintSheet(currentViewingRequest);
            }}
        }}

        function debounceFilter() {{
            clearTimeout(filterDebounceTimer);
            filterDebounceTimer = setTimeout(filterRecords, 200);
        }}

        function filterRecords() {{
            const search = document.getElementById('grid-search').value.toLowerCase().trim();
            const status = document.getElementById('grid-filter-status').value;

            const filtered = allRequests.filter(r => {{
                const matchSearch = !search ||
                    (r.code && r.code.toLowerCase().includes(search)) ||
                    (r.customer_name && r.customer_name.toLowerCase().includes(search)) ||
                    (r.contract_sales && r.contract_sales.toLowerCase().includes(search)) ||
                    (r.service_desc && r.service_desc.toLowerCase().includes(search)) ||
                    (r.technician && r.technician.toLowerCase().includes(search));

                let matchStatus = true;
                if (status === 'cert_done') matchStatus = r.cert_done == 1;
                else if (status === 'cert_pending') matchStatus = !r.cert_done;
                else if (status === 'device_done') matchStatus = r.device_done == 1;
                else if (status === 'device_pending') matchStatus = !r.device_done;

                return matchSearch && matchStatus;
            }});

            renderGridRows(filtered);
        }}

        function renderGrid() {{
            filterRecords();
        }}

        function renderGridRows(list) {{
            const tbody = document.getElementById('grid-tbody');
            const emptyEl = document.getElementById('grid-empty');
            tbody.innerHTML = '';

            if (list.length === 0) {{
                emptyEl.classList.remove('hidden');
                return;
            }}
            emptyEl.classList.add('hidden');

            const isAdmin = currentUser && currentUser.role === 'admin';

            list.forEach((r, idx) => {{
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-slate-50 transition border-b border-slate-200 text-sm';

                let qty = 1;
                try {{
                    const devs = Array.isArray(r.devices) ? r.devices : JSON.parse(r.devices_json || '[]');
                    if (devs.length > 0) {{
                        qty = devs.reduce((sum, item) => sum + (parseInt(item.qty) || 1), 0);
                    }}
                }} catch (e) {{}}

                const recPerson = r.received_person || r.recipient_person || (r.received_info && r.received_info.includes('_') ? r.received_info.split('_')[1] : '') || '—';
                const recDate = r.received_date || (r.received_info && r.received_info.includes('_') ? r.received_info.split('_')[0] : (r.received_info || '—'));
                const retPerson = r.returned_person || r.handover_person || (r.returned_info && r.returned_info.includes('_') ? r.returned_info.split('_')[1] : '') || '—';
                const retDate = r.returned_date || (r.returned_info && r.returned_info.includes('_') ? r.returned_info.split('_')[0] : (r.returned_info || r.expected_return_date || '—'));
                const nextCal = r.next_cal_date || '—';

                tr.innerHTML = `
                    <td class="p-3 text-center font-bold text-slate-500">${{idx + 1}}</td>
                    <td class="p-3 text-center">
                        <button type="button" onclick="openPrintFor('${{r.code}}')" title="Xem & In phiếu yêu cầu"
                            class="px-2.5 py-1 rounded-lg text-xs font-mono font-bold bg-slate-100 text-slate-800 hover:bg-red-50 hover:text-digi border border-slate-300 transition">
                            ${{r.code}}
                        </button>
                    </td>
                    <td class="p-3 font-semibold whitespace-pre-line text-slate-700">${{r.contract_sales || '—'}}</td>
                    <td class="p-3 text-slate-900 font-medium max-w-[280px]">${{r.service_desc || '—'}}</td>
                    <td class="p-3 font-bold text-slate-900 max-w-[240px]">${{r.customer_name || '—'}}</td>
                    
                    <!-- 4 Mã mẫu: Mỗi mã nằm trên 1 hàng riêng biệt, căn lề thẳng hàng, tuyệt đối không dùng dấu phẩy -->
                    <td class="p-2 text-center align-middle">${{formatSampleCodeCell(r.code_temp)}}</td>
                    <td class="p-2 text-center align-middle">${{formatSampleCodeCell(r.code_hum)}}</td>
                    <td class="p-2 text-center align-middle">${{formatSampleCodeCell(r.code_press)}}</td>
                    <td class="p-2 text-center align-middle">${{formatSampleCodeCell(r.code_gas)}}</td>

                    <td class="p-3 text-center font-bold text-slate-800">${{qty}}</td>
                    <td class="p-3 text-right font-mono font-bold text-slate-900 whitespace-nowrap">${{formatCurrency(r.revenue || 0)}}</td>
                    <td class="p-3 font-semibold text-slate-800">${{r.technician || '—'}}</td>
                    
                    <!-- 5 Cột chuẩn ISO: Người nhận PTĐ, Ngày nhận PTĐ, Người trả PTĐ, Ngày trả PTĐ, Ngày hiệu chuẩn tiếp theo -->
                    <td class="p-3 font-medium text-slate-800 whitespace-nowrap">${{recPerson}}</td>
                    <td class="p-3 text-center font-mono text-slate-700 whitespace-nowrap">${{recDate}}</td>
                    <td class="p-3 font-medium text-slate-800 whitespace-nowrap">${{retPerson}}</td>
                    <td class="p-3 text-center font-mono text-slate-700 whitespace-nowrap">${{retDate}}</td>
                    <td class="p-3 text-center font-mono font-semibold text-slate-900 whitespace-nowrap">${{nextCal}}</td>

                    <!-- Checkboxes: Xuất GCN & Giao PTĐ -->
                    <td class="p-2 text-center">
                        <input type="checkbox" ${{r.cert_done ? 'checked' : ''}} ${{isAdmin ? `onchange="toggleQuickStatus(${{r.id}}, 'cert_done', this.checked)"` : 'disabled'}}
                            class="rounded text-slate-700 focus:ring-slate-500 h-5 w-5 cursor-pointer">
                    </td>
                    <td class="p-2 text-center">
                        <input type="checkbox" ${{r.device_done ? 'checked' : ''}} ${{isAdmin ? `onchange="toggleQuickStatus(${{r.id}}, 'device_done', this.checked)"` : 'disabled'}}
                            class="rounded text-slate-700 focus:ring-slate-500 h-5 w-5 cursor-pointer">
                    </td>

                    <td class="p-3 text-slate-600 max-w-[160px] truncate" title="${{r.general_note || ''}}">${{r.general_note || '—'}}</td>

                    <!-- Thao tác với FontAwesome Icons -->
                    <td class="p-3 text-center whitespace-nowrap">
                        ${{isAdmin ? `
                            <button type="button" onclick="openEditModal(${{r.id}})" title="Sửa chi tiết"
                                class="p-2 text-slate-600 hover:text-blue-600 hover:bg-slate-100 rounded-xl transition text-sm">
                                <i class="fa-solid fa-pen-to-square"></i>
                            </button>
                            <button type="button" onclick="handleDeleteRequest(${{r.id}}, '${{r.code}}')" title="Xóa bản ghi"
                                class="p-2 text-slate-500 hover:text-red-600 hover:bg-slate-100 rounded-xl transition text-sm ml-1">
                                <i class="fa-solid fa-trash-can"></i>
                            </button>
                        ` : `
                            <button type="button" onclick="openPrintFor('${{r.code}}')" title="Xem & In"
                                class="px-3 py-1.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-lg transition flex items-center space-x-1">
                                <i class="fa-solid fa-eye"></i><span>Xem/In</span>
                            </button>
                        `}}
                    </td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        function openPrintFor(code) {{
            const req = allRequests.find(r => r.code === code);
            if (req) {{
                currentViewingRequest = req;
                switchTab(2);
                renderPrintSheet(req);
            }}
        }}

        async function toggleQuickStatus(reqId, field, value) {{
            if (!currentUser || currentUser.role !== 'admin') {{
                showToast('Chỉ Quản trị viên mới có quyền cập nhật trạng thái!', 'warning');
                return;
            }}

            try {{
                const res = await fetch(`/api/requests/${{reqId}}/toggle-status`, {{
                    method: 'PATCH',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ field, value }})
                }});
                if (res.ok) {{
                    const r = allRequests.find(item => item.id === reqId);
                    if (r) r[field] = value ? 1 : 0;
                    updateDashboardStats();
                    showToast('Đã cập nhật trạng thái!', 'success');
                }}
            }} catch (e) {{
                const r = allRequests.find(item => item.id === reqId);
                if (r) r[field] = value ? 1 : 0;
                localStorage.setItem('digi_cal_requests', JSON.stringify(allRequests));
                updateDashboardStats();
                showToast('Đã lưu trạng thái cục bộ!', 'success');
            }}
        }}

        function handleExportExcel() {{
            if (!currentUser || currentUser.role !== 'admin') {{
                showToast('Chỉ Quản trị viên (CST@digivn.com) mới có quyền xuất file Excel!', 'warning');
                return;
            }}
            showToast('Đang tạo và tải file Excel chuẩn ISO...', 'info');
            window.location.href = '/api/export-excel';
        }}

        async function handleDeleteRequest(reqId, code) {{
            if (!currentUser || currentUser.role !== 'admin') {{
                showToast('Chỉ Quản trị viên (CST@digivn.com) mới có quyền xóa bản ghi!', 'warning');
                return;
            }}

            if (!confirm(`Bạn có chắc chắn muốn xóa bản ghi phiếu ${{code}} khỏi Sổ theo dõi không? Thao tác này không thể hoàn tác.`)) {{
                return;
            }}

            try {{
                const res = await fetch(`/api/requests/${{reqId}}`, {{ method: 'DELETE' }});
                const result = await res.json();
                if (res.ok && result.success) {{
                    showToast(`Đã xóa thành công phiếu ${{code}}!`, 'success');
                    await loadRequestsData();
                }} else {{
                    showToast(result.error || 'Lỗi khi xóa', 'error');
                }}
            }} catch (e) {{
                allRequests = allRequests.filter(r => r.id !== reqId);
                localStorage.setItem('digi_cal_requests', JSON.stringify(allRequests));
                showToast(`Đã xóa phiếu ${{code}} khỏi bộ nhớ cục bộ!`, 'success');
                renderGrid();
                updateDashboardStats();
            }}
        }}

        function openEditModal(reqId) {{
            if (!currentUser || currentUser.role !== 'admin') {{
                showToast('Chỉ Quản trị viên mới có quyền sửa thông tin!', 'warning');
                return;
            }}

            const req = allRequests.find(r => r.id === reqId);
            if (!req) return;

            document.getElementById('edit-id').value = req.id;
            document.getElementById('edit-modal-code').textContent = `Mã phiếu: ${{req.code}}`;
            document.getElementById('edit-contract').value = req.contract_sales || '';
            document.getElementById('edit-customer').value = req.customer_name || '';
            document.getElementById('edit-desc').value = req.service_desc || '';
            document.getElementById('edit-code-temp').value = formatToLines(req.code_temp);
            document.getElementById('edit-code-hum').value = formatToLines(req.code_hum);
            document.getElementById('edit-code-press').value = formatToLines(req.code_press);
            document.getElementById('edit-code-gas').value = formatToLines(req.code_gas);
            document.getElementById('edit-revenue').value = req.revenue || 0;
            document.getElementById('edit-technician').value = req.technician || '';
            document.getElementById('edit-received-person').value = req.received_person || req.recipient_person || (req.received_info && req.received_info.includes('_') ? req.received_info.split('_')[1] : '') || '';
            document.getElementById('edit-received-date').value = req.received_date || (req.received_info && req.received_info.includes('_') ? req.received_info.split('_')[0] : (req.received_info || '')) || '';
            document.getElementById('edit-returned-person').value = req.returned_person || req.handover_person || (req.returned_info && req.returned_info.includes('_') ? req.returned_info.split('_')[1] : '') || '';
            document.getElementById('edit-returned-date').value = req.returned_date || (req.returned_info && req.returned_info.includes('_') ? req.returned_info.split('_')[0] : (req.returned_info || req.expected_return_date || '')) || '';
            document.getElementById('edit-next-cal-date').value = req.next_cal_date || '';
            document.getElementById('edit-cert-done').checked = !!req.cert_done;
            document.getElementById('edit-device-done').checked = !!req.device_done;
            document.getElementById('edit-note').value = req.general_note || '';

            document.getElementById('edit-modal').classList.remove('hidden');
        }}

        function closeEditModal() {{
            document.getElementById('edit-modal').classList.add('hidden');
        }}

        async function handleSaveEdit(e) {{
            e.preventDefault();
            const id = parseInt(document.getElementById('edit-id').value);
            const req = allRequests.find(r => r.id === id);
            if (!req) return;

            const updatedData = {{
                contract_sales: document.getElementById('edit-contract').value.trim(),
                customer_name: document.getElementById('edit-customer').value.trim(),
                service_desc: document.getElementById('edit-desc').value.trim(),
                code_temp: getCleanSampleCodes('edit-code-temp'),
                code_hum: getCleanSampleCodes('edit-code-hum'),
                code_press: getCleanSampleCodes('edit-code-press'),
                code_gas: getCleanSampleCodes('edit-code-gas'),
                revenue: parseFloat(document.getElementById('edit-revenue').value) || 0,
                technician: document.getElementById('edit-technician').value.trim(),
                received_person: document.getElementById('edit-received-person').value.trim(),
                received_date: document.getElementById('edit-received-date').value.trim(),
                returned_person: document.getElementById('edit-returned-person').value.trim(),
                returned_date: document.getElementById('edit-returned-date').value.trim(),
                next_cal_date: document.getElementById('edit-next-cal-date').value.trim(),
                handover_person: document.getElementById('edit-returned-person').value.trim(),
                recipient_person: document.getElementById('edit-received-person').value.trim(),
                cert_done: document.getElementById('edit-cert-done').checked ? 1 : 0,
                device_done: document.getElementById('edit-device-done').checked ? 1 : 0,
                general_note: document.getElementById('edit-note').value.trim()
            }};

            try {{
                const res = await fetch(`/api/requests/${{id}}`, {{
                    method: 'PUT',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify(updatedData)
                }});
                const result = await res.json();
                if (res.ok && result.success) {{
                    showToast('Cập nhật phiếu thành công!', 'success');
                    closeEditModal();
                    await loadRequestsData();
                }} else {{
                    showToast(result.error || 'Lỗi cập nhật', 'error');
                }}
            }} catch (err) {{
                Object.assign(req, updatedData);
                localStorage.setItem('digi_cal_requests', JSON.stringify(allRequests));
                showToast('Đã lưu thay đổi vào bộ nhớ cục bộ!', 'success');
                closeEditModal();
                renderGrid();
                updateDashboardStats();
            }}
        }}

        // ----------------- UTILITIES -----------------
        function formatCurrency(amount) {{
            if (!amount || isNaN(amount)) return '0 VNĐ';
            return new Intl.NumberFormat('vi-VN').format(amount) + ' VNĐ';
        }}

        function formatDateVN(dateStr) {{
            if (!dateStr) return '';
            const d = new Date(dateStr);
            if (isNaN(d.getTime())) return dateStr;
            return `${{String(d.getDate()).padStart(2, '0')}}/${{String(d.getMonth() + 1).padStart(2, '0')}}/${{d.getFullYear()}}`;
        }}

        function showToast(message, type = 'info') {{
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = `p-3.5 px-5 rounded-2xl shadow-xl text-sm font-extrabold pointer-events-auto transform transition-all duration-300 flex items-center space-x-2.5 text-white ${{
                type === 'success' ? 'bg-emerald-600' :
                type === 'warning' ? 'bg-amber-600' :
                type === 'error' ? 'bg-digi' : 'bg-slate-900'
            }}`;
            
            let iconHtml = '<i class="fa-solid fa-circle-info"></i>';
            if (type === 'success') iconHtml = '<i class="fa-solid fa-circle-check"></i>';
            if (type === 'warning') iconHtml = '<i class="fa-solid fa-triangle-exclamation"></i>';
            if (type === 'error') iconHtml = '<i class="fa-solid fa-circle-xmark"></i>';

            toast.innerHTML = `
                <span class="text-base">${{iconHtml}}</span>
                <span>${{message}}</span>
            `;
            container.appendChild(toast);
            setTimeout(() => {{
                toast.classList.add('opacity-0', 'translate-y-2');
                setTimeout(() => toast.remove(), 300);
            }}, 3500);
        }}
    </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated index.html successfully! Size: {len(html_content)} bytes")
