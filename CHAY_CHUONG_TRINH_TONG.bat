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
if "%~1"=="1" goto opt_custom
if "%~1"=="2" goto opt_tui
if "%~1"=="3" goto opt_advanced
if "%~1"=="4" goto opt_charts
if "%~1"=="5" goto opt_tong_hop
if "%~1"=="6" goto opt_verify
if "%~1"=="7" goto opt_setup
if /i "%~1"=="--custom" goto opt_custom
if /i "%~1"=="--tui" goto opt_tui
if /i "%~1"=="--verify" goto opt_verify
if /i "%~1"=="--charts" goto opt_charts
if /i "%~1"=="--tonghop" goto opt_tong_hop
if /i "%~1"=="--setup" goto opt_setup

:: Neu nguoi dung truyen tham so CLI truc tiep (vi du: --graph, --all, -h...), thuc thi thang main.py
if not "%~1"=="" (
    "%PYTHON_CMD%" "%SCRIPT_DIR%main.py" %*
    exit /b %ERRORLEVEL%
)

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
echo  * Bo Do thi Benchmark     : 30 Do thi Chuan Quoc Te (pbodulieu)
echo ================================================================================
echo.
echo  --- [A] CHUONG TRINH THUC NGHIEM MO HINH (EVO-RL MSCC) ---
echo   [1]  Dien Ten Hoac Dan Danh Sach Do Thi Tuy Chon
echo   [2]  Che Do Chon Do Thi Tuong Tac TUI (Dung phim mui ten, Space, Enter)
echo   [3]  Tuy Chinh Sieu Tham So Nang Cao (s, seeds, workers, epochs, pop_size)
echo.
echo  --- [B] XUAT BIEU DO, SO LIEU VA BAO CAO KHOA HOC ---
echo   [4]  Xuat Bieu Do Phan Tich va Hoi Tu (Chart_seed: 600 DPI PNG va Vector PDF)
echo   [5]  Tong Hop Bang So Lieu Phan Tich va Kiem Dinh Thong Ke Wilcoxon
echo.
echo  --- [C] CONG CU VA TIEN ICH HE THONG ---
echo   [6]  Kiem Tra Toan Dien He Thong (9 Giai doan kiem chung tu dong)
echo   [7]  Thiet Lap Moi Truong va Kiem Tra GPU NVIDIA CUDA
echo.
echo   [0]  Thoat chuong trinh
echo ================================================================================
echo.

set "main_choice="
set /p main_choice=">> Nhap so chuc nang ban muon chon (0-7): "

if "%main_choice%"=="1" goto opt_custom
if "%main_choice%"=="2" goto opt_tui
if "%main_choice%"=="3" goto opt_advanced
if "%main_choice%"=="4" goto opt_charts
if "%main_choice%"=="5" goto opt_tong_hop
if "%main_choice%"=="6" goto opt_verify
if "%main_choice%"=="7" goto opt_setup
if "%main_choice%"=="0" goto exit_master

echo.
echo [!] Lua chon khong hop le. Vui long nhap tu 0 den 7.
timeout /t 2 >nul 2>&1
goto main_menu

:: ============================================================================
:: [1] DIEN TEN HOAC DAN DANH SACH DO THI TUY CHON
:: ============================================================================
:opt_custom
cls
echo ================================================================================
echo    [1] DIEN TEN HOAC DAN DANH SACH DO THI BAT KY DE CHAY
echo ================================================================================
echo  Huong dan:
echo   - Nhap mot hoac nhieu ten do thi cach nhau boi dau phay (,) hoac dau cach.
echo   - Ho tro dan (paste) toan bo danh sach do thi tu ban phim.
echo   - Khong bat buoc phai co duoi file (vi du: karate hay karate.clq deu duoc).
echo ================================================================================
echo.
set "custom_graphs="
set /p custom_graphs=">> Nhap / Dan danh sach do thi (hoac '0' de quay lai): "
if "%custom_graphs%"=="" (
    echo [!] Ban chua nhap ten do thi nao.
    echo.
    pause
    goto main_menu
)
if "%custom_graphs%"=="0" goto main_menu
if /i "%custom_graphs%"=="q" goto main_menu
if /i "%custom_graphs%"=="exit" goto main_menu
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
:: [2] CHE DO CHON DO THI TUONG TAC TUI
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
:: [3] TUY CHINH SIEU THAM SO NANG CAO
:: ============================================================================
:opt_advanced
cls
echo ================================================================================
echo    [3] TUY CHINH SIEU THAM SO THUAT TOAN NANG CAO
echo ================================================================================
set "dset_in="
set /p dset_in=">> Danh sach do thi (hoac 'all' / ten do thi, '0' de quay lai) [mac dinh 'karate,jazz']: "
if "%dset_in%"=="0" goto main_menu
if /i "%dset_in%"=="q" goto main_menu
if /i "%dset_in%"=="exit" goto main_menu
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
:: [4] XUAT BIEU DO PHAN TICH VA HOI TU
:: ============================================================================
:opt_charts
cls
call "%SCRIPT_DIR%Run.bat\runbieudo.bat"
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [5] TONG HOP SO LIEU PHAN TICH VA DONG GOI BAO CAO
:: ============================================================================
:opt_tong_hop
cls
call "%SCRIPT_DIR%Run.bat\run_tong_hop_so_lieu.bat"
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [6] KIEM TRA TOAN DIEN HE THONG (9 GIAI DOAN)
:: ============================================================================
:opt_verify
cls
call "%SCRIPT_DIR%Run.bat\verify_all.bat"
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [7] THIET LAP MOI TRUONG VA KIEM TRA GPU
:: ============================================================================
:opt_setup
cls
call "%SCRIPT_DIR%setup.bat" --no-launch
echo.
echo ================================================================================
echo [V] Hoan tat kiem tra moi truong va GPU CUDA.
echo ================================================================================
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [0] THOAT
:: ============================================================================
:exit_master
echo.
echo [*] Cam on ban da su dung He thong Phan mem NCKH EVO-RL MSCC. Tam biet!
exit /b 0
