@echo off
setlocal
chcp 65001 >nul
title HE THONG PHAN MEM NCKH: EVO-RL MSCC FRAMEWORK

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

set "PYTHONUNBUFFERED=1"
set "PYTHONIOENCODING=utf-8"

:: ============================================================================
:: TU DONG NHAN DIEN MOI TRUONG PYTHON (Venv, Conda, He thong)
:: ============================================================================
set "PYTHON_CMD=python"
if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    set "PYTHON_CMD=%SCRIPT_DIR%.venv\Scripts\python.exe"
) else if exist "%~d0\conda\python.exe" (
    set "PYTHON_CMD=%~d0\conda\python.exe"
) else if exist "A:\conda\python.exe" (
    set "PYTHON_CMD=A:\conda\python.exe"
) else if exist "C:\conda\python.exe" (
    set "PYTHON_CMD=C:\conda\python.exe"
) else if exist "D:\conda\python.exe" (
    set "PYTHON_CMD=D:\conda\python.exe"
) else if exist "%USERPROFILE%\miniconda3\python.exe" (
    set "PYTHON_CMD=%USERPROFILE%\miniconda3\python.exe"
) else if exist "%USERPROFILE%\anaconda3\python.exe" (
    set "PYTHON_CMD=%USERPROFILE%\anaconda3\python.exe"
) else if exist "C:\ProgramData\anaconda3\python.exe" (
    set "PYTHON_CMD=C:\ProgramData\anaconda3\python.exe"
) else if exist "C:\miniconda3\python.exe" (
    set "PYTHON_CMD=C:\miniconda3\python.exe"
)

:: Kiem tra doi so dong lenh truc tiep (neu co)
if "%~1"=="0" goto exit_master
if "%~1"=="1" goto opt_demo
if "%~1"=="2" goto opt_type1
if "%~1"=="3" goto opt_type2
if "%~1"=="4" goto opt_all
if "%~1"=="5" goto opt_custom
if "%~1"=="6" goto opt_tui
if "%~1"=="7" goto opt_advanced
if "%~1"=="8" goto opt_charts
if "%~1"=="9" goto opt_tong_hop
if "%~1"=="10" goto opt_verify
if "%~1"=="11" goto opt_setup
if /i "%~1"=="--demo" goto opt_demo
if /i "%~1"=="--all" goto opt_all
if /i "%~1"=="--verify" goto opt_verify
if /i "%~1"=="--charts" goto opt_charts
if /i "%~1"=="--tonghop" goto opt_tong_hop
if /i "%~1"=="--setup" goto opt_setup

:: ============================================================================
:: MENU DIEU KHIEN CHINH TRUC QUAN (MASTER CONSOLE MENU)
:: ============================================================================
:main_menu
cls
echo ================================================================================
echo      HE THONG PHAN MEM NCKH: EVO-RL MINIMUM s-CLUB COVER FRAMEWORK
echo       Toi Uu Hoa Tien Hoa Ket Hop Hoc Tang Cuong Sau Thich Nghi (PPO-AOS)
echo ================================================================================
echo  * Trinh thong dich Python : %PYTHON_CMD%
echo  * Moi truong tang toc     : GPU NVIDIA CUDA / Da tien trinh CPU (10 Workers)
echo  * Bo 30 Do thi Benchmark  : 12 Mang thuc te Type 1 + 18 DIMACS Type 2
echo ================================================================================
echo.
echo  --- [A] CHUONG TRINH THUC NGHIEM MÔ HÌNH (EVO-RL MSCC) ---
echo   [1]  Chay Test Nhanh (Demo 4 do thi: karate, chesapeake, dolphins, johnson8-2-4)
echo   [2]  Chay Nhom 1 - 12 Mang Thuc Te (Type 1: karate, jazz, email, netscience...)
echo   [3]  Chay Nhom 2 - 18 Do Thi DIMACS (Type 2: johnson, brock, gen, san, hamming...)
echo   [4]  Chay Toan Bo 30 Do Thi Benchmark Chuan Quoc Te (Type 1 + Type 2)
echo   [5]  Dien Ten Hoac Dan Danh Sach Do Thi Tuy Chon
echo   [6]  Che Do Chon Do Thi Tuong Tac TUI (Dung phim mui ten, Space, Enter)
echo   [7]  Tuy Chinh Sieu Tham So Nang Cao (s, seeds, workers, epochs, pop_size)
echo.
echo  --- [B] XUAT BIEU DO, SO LIEU VA BAO CAO KHOA HOC ---
echo   [8]  Xuat Bieu Do Phan Tich va Hoi Tu (Chart_seed: 600 DPI PNG va Vector PDF)
echo   [9]  Tong Hop Bang So Lieu Phan Tich va Kiem Dinh Thong Ke Wilcoxon
echo.
echo  --- [C] CONG CU VA TIEN ICH HE THONG ---
echo   [10] Kiem Tra Toan Dien He Thong (9 Giai doan kiem chung tu dong)
echo   [11] Thiet Lap Moi Truong va Kiem Tra GPU NVIDIA CUDA
echo.
echo   [0]  Thoat chuong trinh
echo ================================================================================
echo.

set "main_choice="
set /p main_choice=">> Nhap so chuc nang ban muon chon (0-11): "

if "%main_choice%"=="1" goto opt_demo
if "%main_choice%"=="2" goto opt_type1
if "%main_choice%"=="3" goto opt_type2
if "%main_choice%"=="4" goto opt_all
if "%main_choice%"=="5" goto opt_custom
if "%main_choice%"=="6" goto opt_tui
if "%main_choice%"=="7" goto opt_advanced
if "%main_choice%"=="8" goto opt_charts
if "%main_choice%"=="9" goto opt_tong_hop
if "%main_choice%"=="10" goto opt_verify
if "%main_choice%"=="11" goto opt_setup
if "%main_choice%"=="0" goto exit_master

echo.
echo [!] Lua chon khong hop le. Vui long nhap tu 0 den 11.
timeout /t 2 >nul 2>&1
goto main_menu

:: ============================================================================
:: [1] CHAY TEST NHANH (DEMO 4 DO THI)
:: ============================================================================
:opt_demo
cls
echo ================================================================================
echo    [1] CHAY TEST NHANH DEMO (karate, chesapeake, dolphins, johnson8-2-4)
echo ================================================================================
echo.
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "karate,chesapeake,dolphins,johnson8-2-4"
echo.
echo ================================================================================
echo [V] Hoan thanh chay Test Demo.
echo ================================================================================
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [2] CHAY NHOM 1 (12 MANG THUC TE)
:: ============================================================================
:opt_type1
cls
echo ================================================================================
echo    [2] CHAY 12 DO THI NHOM TYPE 1 (REAL-WORLD COMPLEX NETWORKS)
echo ================================================================================
echo.
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "karate,chesapeake,dolphins,lesmis,polbooks,adjnoun,football,jazz,celegansneural,netscience,celegans_metabolic,email"
echo.
echo ================================================================================
echo [V] Hoan thanh thuc nghiem Nhom 1 (Type 1).
echo ================================================================================
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [3] CHAY NHOM 2 (18 DO THI DIMACS)
:: ============================================================================
:opt_type2
cls
echo ================================================================================
echo    [3] CHAY 18 DO THI NHOM TYPE 2 (DIMACS CLIQUE BENCHMARK)
echo ================================================================================
echo.
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "johnson8-2-4,hamming6-2,hamming6-4,johnson8-4-4,MANN_a9,C125.9,johnson16-2-4,keller4,c-fat200-1,c-fat200-5,brock200_1,brock200_2,brock200_3,gen200_p0.9_44,gen200_p0.9_55,san200_0.9_2,san200_0.9_3,hamming8-2"
echo.
echo ================================================================================
echo [V] Hoan thanh thuc nghiem Nhom 2 (Type 2).
echo ================================================================================
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [4] CHAY TOAN BO 30 DO THI BENCHMARK
:: ============================================================================
:opt_all
cls
echo ================================================================================
echo    [4] CHAY TOAN BO 30 DO THI BENCHMARK CHUAN QUOC TE (TYPE 1 + TYPE 2)
echo ================================================================================
echo.
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --all
echo.
echo ================================================================================
echo [V] Hoan thanh thuc nghiem toan bo 30 do thi benchmark.
echo ================================================================================
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [5] DIEN TEN HOAC DAN DANH SACH DO THI TUY CHON
:: ============================================================================
:opt_custom
cls
echo ================================================================================
echo    [5] DIEN TEN HOAC DAN DANH SACH DO THI BAT KY DE CHAY
echo ================================================================================
echo  Huong dan:
echo   - Nhap mot hoac nhieu ten do thi cach nhau boi dau phay (,) hoac dau cach.
echo   - Ho tro dan (paste) toan bo danh sach do thi tu ban phim.
echo   - Khong bat buoc phai co duoi file (vi du: karate hay karate.clq deu duoc).
echo ================================================================================
echo.
set "custom_graphs="
set /p custom_graphs=">> Nhap / Dan danh sach do thi: "
if "%custom_graphs%"=="" (
    echo [!] Ban chua nhap ten do thi nao.
    echo.
    pause
    goto main_menu
)
echo.
echo [*] Dang chuyen danh sach do thi sang bo xu ly EVO-RL...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "%custom_graphs%"
echo.
echo ================================================================================
echo [V] Hoan thanh thuc nghiem tren danh sach do thi tuy chon.
echo ================================================================================
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [6] CHE DO CHON DO THI TUONG TAC TUI
:: ============================================================================
:opt_tui
cls
echo [*] Mo giao dien tuong tac chon do thi TUI (Interactive Keyboard Navigation)...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --tui
echo.
echo ================================================================================
echo [V] Hoan thanh phien chon do thi TUI.
echo ================================================================================
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [7] TUY CHINH SIEU THAM SO NANG CAO
:: ============================================================================
:opt_advanced
cls
echo ================================================================================
echo    [7] TUY CHINH SIEU THAM SO THUAT TOAN NANG CAO
echo ================================================================================
set "dset_in="
set /p dset_in=">> Danh sach do thi (hoac 'all' / ten do thi) [mac dinh 'karate,jazz']: "
if "%dset_in%"=="" set "dset_in=karate,jazz"
set "s_in="
set /p s_in=">> Nguong duong kinh s-club (s) [mac dinh 2]: "
if "%s_in%"=="" set "s_in=2"
set "seed_in="
set /p seed_in=">> So luong hat giong ngau nhien (Seeds) [mac dinh 20]: "
if "%seed_in%"=="" set "seed_in=20"
set "worker_in="
set /p worker_in=">> So workers chay song song (Workers) [mac dinh 10]: "
if "%worker_in%"=="" set "worker_in=10"
set "epoch_in="
set /p epoch_in=">> So the he toi da (Epochs/Generations) [mac dinh 200]: "
if "%epoch_in%"=="" set "epoch_in=200"
set "pop_in="
set /p pop_in=">> Kich thuoc quan the (Pop Size) [mac dinh 100]: "
if "%pop_in%"=="" set "pop_in=100"

echo.
echo [*] Dang khoi chay voi cau hinh tuy chinh...
if /i "%dset_in%"=="all" (
    "%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --all --s %s_in% --seeds %seed_in% --workers %worker_in% --epochs %epoch_in% --pop_size %pop_in%
) else (
    "%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "%dset_in%" --s %s_in% --seeds %seed_in% --workers %worker_in% --epochs %epoch_in% --pop_size %pop_in%
)
echo.
echo ================================================================================
echo [V] Hoan thanh thuc nghiem voi tham so tuy chinh.
echo ================================================================================
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [8] XUAT BIEU DO PHAN TICH VA HOI TU
:: ============================================================================
:opt_charts
cls
call "%SCRIPT_DIR%Run.bat\runbieudo.bat"
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [9] TONG HOP SO LIEU PHAN TICH VA DONG GOI BAO CAO
:: ============================================================================
:opt_tong_hop
cls
call "%SCRIPT_DIR%Run.bat\run_tong_hop_so_lieu.bat"
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [10] KIEM TRA TOAN DIEN HE THONG (9 GIAI DOAN)
:: ============================================================================
:opt_verify
cls
call "%SCRIPT_DIR%Run.bat\verify_all.bat"
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [11] THIET LAP MOI TRUONG VA KIEM TRA GPU
:: ============================================================================
:opt_setup
cls
call "%SCRIPT_DIR%setup.bat" --no-launch
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [0] THOAT
:: ============================================================================
:exit_master
echo.
echo [*] Cam on ban da su dung He thong Phan mem NCKH EVO-RL MSCC. Tam biet!
exit /b 0
