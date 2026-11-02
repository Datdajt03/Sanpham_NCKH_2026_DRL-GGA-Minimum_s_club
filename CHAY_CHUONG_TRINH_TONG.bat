@echo off
setlocal
chcp 65001 >nul
title CHUONG TRINH TONG QUAN LY VA VAN HANH TOAN DIEN - EVO-RL MSCC

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

set "PYTHONUNBUFFERED=1"
set "PYTHONIOENCODING=utf-8"

:: ============================================================================
:: TU DONG NHAN DIEN MOI TRUONG PYTHON (Conda, Venv, He thong)
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
if "%~1"=="1" goto opt_bai1
if "%~1"=="2" goto opt_bai2
if "%~1"=="3" goto opt_bai3
if "%~1"=="4" goto opt_both
if "%~1"=="5" goto opt_charts
if "%~1"=="6" goto opt_tong_hop
if "%~1"=="7" goto opt_regen_md
if "%~1"=="8" goto opt_verify
if "%~1"=="9" goto opt_setup
if /i "%~1"=="--verify" goto opt_verify
if /i "%~1"=="--charts" goto opt_charts
if /i "%~1"=="--tonghop" goto opt_tong_hop

:: ============================================================================
:: MENU DIEU KHIEN CHINH (MASTER CONSOLE)
:: ============================================================================
:main_menu
cls
echo ================================================================================
echo     HE THONG PHAN MEM TONG HOP NCKH - TOI UU HOA TIEN HOA KET HOP DEEP RL
echo      (EVO-RL Minimum s-Club Cover Framework - Hybrid Parallel Architecture)
echo ================================================================================
echo  * Trinh thong dich Python: %PYTHON_CMD%
echo  * Moi truong tang toc: GPU NVIDIA CUDA / Da nhan CPU Multi-processing (10 Workers)
echo  * Bo 30 Do thi Benchmark chuan quoc te: 12 Real-world Type 1 + 18 DIMACS Type 2
echo ================================================================================
echo.
echo  --- CHUONG TRINH THUC NGHIEM VA CHAY MO HINH ---
echo   [1] Chay thuc nghiem Bai 1 (Giai bai toan MSCC voi EVO-RL tren 30 do thi benchmark)
echo   [2] Chay thuc nghiem Bai 2 (Danh gia tinh phu hop cua Deep RL: PPO, MAB, Greedy, Random)
echo   [3] Chay thuc nghiem Bai 3 (Phan tich chi phi thoi gian, overhead va diem hoa von cua Deep RL)
echo   [4] Chay dong thoi ca Bai 2 va Bai 3 (Chay tu dong song song de tiet kiem thoi gian)
echo.
echo  --- XUAT KET QUA, BIEU DO VA BAO CAO ---
echo   [5] Xuat bieu do phan tich va hoi tu (Xuat bieu do do phan giai cao dang PNG va PDF)
echo   [6] Tong hop so lieu phan tich (Tap phu [C], Thoi gian chay, So lan danh gia, Chi phi Overhead)
echo   [7] Tao lai bao cao Markdown cho Bai 2 va Bai 3 (Ket xuat tu file ket qua CSV san co)
echo.
echo  --- TIEN ICH HE THONG VA KIEM TRA ---
echo   [8] Kiem tra toan dien he thong (Xac minh tinh toan ven cua thu vien, tap du lieu va module)
echo   [9] Thiet lap moi truong va kiem tra GPU (Cai dat thu vien can thiet va kiem tra CUDA)
echo.
echo   [0] Thoat chuong trinh
echo ================================================================================
echo.
set "main_choice="
set /p main_choice=">> Nhap so chuc nang ban muon chon (0-9): "

if "%main_choice%"=="1" goto opt_bai1
if "%main_choice%"=="2" goto opt_bai2
if "%main_choice%"=="3" goto opt_bai3
if "%main_choice%"=="4" goto opt_both
if "%main_choice%"=="5" goto opt_charts
if "%main_choice%"=="6" goto opt_tong_hop
if "%main_choice%"=="7" goto opt_regen_md
if "%main_choice%"=="8" goto opt_verify
if "%main_choice%"=="9" goto opt_setup
if "%main_choice%"=="0" goto exit_master

echo.
echo [!] Lua chon khong hop le. Vui long nhap tu 0 den 9.
timeout /t 2 >nul 2>&1
goto main_menu

:: ============================================================================
:: [1] CHAY THUC NGHIEM BAI 1
:: ============================================================================
:opt_bai1
cls
call "%SCRIPT_DIR%Run.bat\run.bat"
echo.
echo ================================================================================
echo Hoan thanh tac vu Bai 1.
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [2] CHAY THUC NGHIEM BAI 2
:: ============================================================================
:opt_bai2
cls
call "%SCRIPT_DIR%Run.bat\run_bai2.bat"
echo.
echo ================================================================================
echo Hoan thanh tac vu Bai 2.
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [3] CHAY THUC NGHIEM BAI 3
:: ============================================================================
:opt_bai3
cls
call "%SCRIPT_DIR%Run.bat\run_bai3.bat"
echo.
echo ================================================================================
echo Hoan thanh tac vu Bai 3.
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [4] CHAY DONG THOI BAI 2 VA BAI 3
:: ============================================================================
:opt_both
cls
call "%SCRIPT_DIR%Run.bat\run_both_bai2_and_bai3.bat"
echo.
echo ================================================================================
echo Hoan thanh tac vu chay song song Bai 2 va Bai 3.
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [5] XUAT BIEU DO PHAN TICH VA HOI TU
:: ============================================================================
:opt_charts
cls
call "%SCRIPT_DIR%Run.bat\runbieudo.bat"
echo.
echo ================================================================================
echo Hoan thanh tac vu xuat bieu do.
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [6] TONG HOP SO LIEU PHAN TICH
:: ============================================================================
:opt_tong_hop
cls
call "%SCRIPT_DIR%Run.bat\run_tong_hop_so_lieu.bat"
echo.
echo ================================================================================
echo Hoan thanh tac vu tong hop so lieu phan tich.
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [7] XUAT LAI BAO CAO MARKDOWN BAI 2 VA BAI 3
:: ============================================================================
:opt_regen_md
cls
echo ================================================================================
echo         TAO LAI HE THONG BAO CAO SO LIEU MARKDOWN BAI 2 VA BAI 3
echo ================================================================================
echo.
echo [*] Dang doc lai du lieu CSV va khoi tao he thong bao cao Markdown Bai 2...
"%PYTHON_CMD%" "%SCRIPT_DIR%Bai_2_DeepRL_AOS_Suitability\analysis_bai2.py"
echo.
echo [*] Dang doc lai du lieu CSV va khoi tao he thong bao cao Markdown Bai 3...
"%PYTHON_CMD%" "%SCRIPT_DIR%Bai_3_Cost_Benefit_Analysis\analysis_bai3.py"
echo.
echo ================================================================================
echo [V] Tat ca bao cao Markdown (.md) da duoc cap nhat thanh cong!
echo     - Bai 2: Bai_2_DeepRL_AOS_Suitability\results_bai2\Tong_hop_so_lieu_Bai_2.md
echo     - Bai 3: Bai_3_Cost_Benefit_Analysis\results_bai3\Tong_hop_so_lieu_Bai_3.md
echo ================================================================================
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [8] KIEM TRA TOAN DIEN HE THONG
:: ============================================================================
:opt_verify
cls
call "%SCRIPT_DIR%Run.bat\verify_all.bat"
echo.
echo ================================================================================
echo Hoan thanh kiem tra he thong.
pause
if not "%~1"=="" exit /b 0
goto main_menu

:: ============================================================================
:: [9] THIET LAP MOI TRUONG VA KIEM TRA GPU
:: ============================================================================
:opt_setup
cls
call "%SCRIPT_DIR%setup.bat"
echo.
echo ================================================================================
echo Hoan thanh thiet lap moi truong.
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
