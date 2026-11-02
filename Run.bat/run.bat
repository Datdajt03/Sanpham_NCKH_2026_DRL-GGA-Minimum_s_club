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

:: Neu nguoi dung truyen tham so tu dong lenh (CLI), thuc thi truc tiep khong qua menu
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
echo  [1] Chay Test Nhanh (Demo: karate, chesapeake, dolphins, johnson8-2-4)
echo  [2] Chay Nhom Type 1 (12 Mang thuc te: karate, jazz, email, netscience...)
echo  [3] Chay Nhom Type 2 (18 Do thi DIMACS: johnson, brock, gen, san, hamming...)
echo  [4] Chay Toan Bo 30 Do Thi Benchmark Chuan (Type 1 + Type 2)
echo  [5] Dien Ten Do Thi Tuy Chon (Nhap / Dan danh sach ten do thi tuy y)
echo  [6] Che do Chon Do Thi Tuong Tac TUI (Dung phim mui ten, Space, Enter)
echo  [7] Tuy chinh Sieu tham so nang cao (s, seeds, workers, epochs, pop_size)
echo  [8] Thoat
echo.
echo ================================================================================

set "choice="
set /p choice=">> Nhap lua chon cua ban (1-8): "

if "%choice%"=="1" goto opt_demo
if "%choice%"=="2" goto opt_type1
if "%choice%"=="3" goto opt_type2
if "%choice%"=="4" goto opt_all_benchmark
if "%choice%"=="5" goto opt_custom_name
if "%choice%"=="6" goto opt_tui
if "%choice%"=="7" goto opt_advanced
if "%choice%"=="8" goto exit_prog
goto invalid

:opt_demo
echo.
echo [*] Bat dau chay Test Demo tren 4 do thi...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "karate,chesapeake,dolphins,johnson8-2-4"
goto end

:opt_type1
echo.
echo [*] Bat dau chay 12 do thi Nhom Type 1 (Real-world Complex Networks)...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "karate,chesapeake,dolphins,lesmis,polbooks,adjnoun,football,jazz,celegansneural,netscience,celegans_metabolic,email"
goto end

:opt_type2
echo.
echo [*] Bat dau chay 18 do thi Nhom Type 2 (DIMACS Clique Instances)...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "johnson8-2-4,hamming6-2,hamming6-4,johnson8-4-4,MANN_a9,C125.9,johnson16-2-4,keller4,c-fat200-1,c-fat200-5,brock200_1,brock200_2,brock200_3,gen200_p0.9_44,gen200_p0.9_55,san200_0.9_2,san200_0.9_3,hamming8-2"
goto end

:opt_all_benchmark
echo.
echo [*] Bat dau chay toan bo 30 do thi Benchmark chuan...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "karate,chesapeake,dolphins,lesmis,polbooks,adjnoun,football,jazz,celegansneural,netscience,celegans_metabolic,email,johnson8-2-4,hamming6-2,hamming6-4,johnson8-4-4,MANN_a9,C125.9,johnson16-2-4,keller4,c-fat200-1,c-fat200-5,brock200_1,brock200_2,brock200_3,gen200_p0.9_44,gen200_p0.9_55,san200_0.9_2,san200_0.9_3,hamming8-2"
goto end

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
set /p custom_graphs=">> Nhap / Dan danh sach do thi: "
if "%custom_graphs%"=="" (
    echo [!] Ban chua nhap ten do thi nao.
    echo.
    pause
    goto menu
)
echo.
echo [*] Dang chuyen danh sach do thi sang bo xu ly EVO-RL...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "%custom_graphs%"
goto end

:opt_tui
echo.
echo [*] Mo giao dien tuong tac chon do thi TUI (Interactive Keyboard Navigation)...
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py"
goto end

:opt_advanced
echo.
echo ================================================================================
echo                      TUY CHINH SIEU THAM SO NANG CAO
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
"%PYTHON_CMD%" "%SCRIPT_DIR%main.py" --graph "%dset_in%" --s %s_in% --seeds %seed_in% --workers %worker_in% --epochs %epoch_in% --pop_size %pop_in%
goto end

:invalid
echo.
echo [!] Lua chon khong hop le. Vui long chon tu 1 den 8.
echo.
pause
goto menu

:end
echo.
echo ================================================================================
echo  [V] Phien chay da hoan tat. Ket qua duoc luu tai thu muc: results/
echo ================================================================================
echo.
pause
goto menu

:exit_prog
echo.
echo Tam biet!
