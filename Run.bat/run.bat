@echo off
setlocal
chcp 65001 >nul
title EVO-RL: Minimum s-Club Cover Framework (Hybrid CPU + GPU)

set "RUN_DIR=%~dp0"
cd /d "%RUN_DIR%.."
set "SCRIPT_DIR=%CD%\"

set "PYTHONUNBUFFERED=1"
set "PYTHONIOENCODING=utf-8"

:: Tu dong nhan dien Python trong Conda hoac moi truong he thong
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
if "%~1"=="0" goto exit_prog
if "%~1"=="1" goto opt_custom_name
if "%~1"=="2" goto opt_tui
if "%~1"=="3" goto opt_advanced
if /i "%~1"=="--tui" goto opt_tui
if /i "%~1"=="--custom" goto opt_custom_name

:: Neu nguoi dung truyen tham so CLI khac (vi du: --graph, --all, -h...), thuc thi truc tiep khong qua menu
if not "%~1"=="" (
    "%PYTHON_CMD%" "%SCRIPT_DIR%main.py" %*
    goto end
)

:menu
cls
echo ================================================================================
echo    HE THONG THUC NGHIEM TIEN HOA HOC TANG CUONG SAU (EVO-RL MSCC)
echo ================================================================================
echo  * Cau hinh mac dinh: 20 Seeds co dinh (seedun.md) - 10 Workers da luong CPU
echo  * Bo tang toc PPO: GPU NVIDIA Tensor Cores / CUDA Auto-Boost
echo ================================================================================
echo.
echo  [1] Dien Ten Do Thi Tuy Chon (Nhap / Dan danh sach ten do thi tuy y)
echo  [2] Che do Chon Do Thi Tuong Tac TUI (Dung phim mui ten, Space, Enter)
echo  [3] Tuy chinh Sieu tham so nang cao (s, seeds, workers, epochs, pop_size)
echo  [0] Thoat
echo.
echo ================================================================================

set "choice="
set /p choice=">> Nhap lua chon cua ban (0-3): "

if "%choice%"=="1" goto opt_custom_name
if "%choice%"=="2" goto opt_tui
if "%choice%"=="3" goto opt_advanced
if "%choice%"=="0" goto exit_prog
goto invalid

:opt_custom_name
echo.
echo ================================================================================
echo            DIEN TEN HOAC DAN DANH SACH DO THI BAT KY DE CHAY
echo ================================================================================
echo  Huong dan:
echo   - Nhap mot hoac nhieu ten do thi cach nhau boi dau phay (,) hoac dau cach.
echo   - Ho tro dan (paste) toan bo danh sach do thi tu ban phim.
echo   - Khong bat buoc phai co duoi file (vi du: karate hay karate.clq deu duoc).
echo   - Sau khi nhan ENTER, he thong se tu dong nhan dien va dem so luong do thi!
echo ================================================================================
echo.
set "custom_graphs="
set /p custom_graphs=">> Nhap / Dan danh sach do thi (hoac '0' de quay lai): "
if "%custom_graphs%"=="" (
    echo [!] Ban chua nhap ten do thi nao.
    echo.
    pause
    goto menu
)
if "%custom_graphs%"=="0" goto menu
if /i "%custom_graphs%"=="q" goto menu
if /i "%custom_graphs%"=="exit" goto menu
echo.
echo [*] Dang chuyen danh sach do thi sang bo xu ly EVO-RL...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "%custom_graphs%"
goto end

:opt_tui
echo.
echo [*] Mo giao dien tuong tac chon do thi TUI (Interactive Keyboard Navigation)...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --tui
goto end

:opt_advanced
echo.
echo ================================================================================
echo                      TUY CHINH SIEU THAM SO NANG CAO
echo ================================================================================
set "dset_in="
set /p dset_in=">> Danh sach do thi (hoac 'all' / ten do thi, '0' de quay lai) [mac dinh 'karate,jazz']: "
if "%dset_in%"=="0" goto menu
if /i "%dset_in%"=="q" goto menu
if /i "%dset_in%"=="exit" goto menu
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
goto end

:invalid
echo.
echo [!] Lua chon khong hop le. Vui long chon tu 0 den 3.
echo.
pause
goto menu

:end
echo.
echo ================================================================================
echo  [V] Phien chay da hoan tat. Ket qua duoc luu tai thu muc: results/
echo ================================================================================
echo.
if not "%~1"=="" exit /b 0
pause
goto menu

:exit_prog
echo.
echo Tam biet!
exit /b 0
