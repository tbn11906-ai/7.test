@echo off
chcp 65001 > nul
title DIGI Technologies - He thong Tiep nhan Hieu chuan & So PTD
echo ===================================================================
echo     DIGI TECHNOLOGIES - PHONG DICH VU & CONG NGHE HIEU CHUAN
echo     He Thong Tiep Nhan Yeu Cau Hieu Chuan & Quan Ly So PTD
echo ===================================================================
echo.
echo [*] Tai khoan Admin: CST@digivn.com  / CST@654
echo [*] Tai khoan Staff: nhanvien@digivn.com / 123456
echo.
echo [1/2] Dang mo trinh duyet tai: http://localhost:5000 ...
timeout /t 2 > nul
start "" "http://localhost:5000"
echo [2/2] Dang khoi dong Web Server Flask (Nhan Ctrl+C de dung)...
python app.py
pause
