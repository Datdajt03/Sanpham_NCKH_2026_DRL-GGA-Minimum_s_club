@echo off
setlocal
chcp 65001 >nul
title RUN CONCURRENT EXPERIMENTS - BAI 2 AND BAI 3

set "RUN_DIR=%~dp0"
cd /d "%RUN_DIR%.."
set "SCRIPT_DIR=%CD%\"

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

set "BAI2_DIR=%SCRIPT_DIR%Bai_2_DeepRL_AOS_Suitability"
if not exist "%BAI2_DIR%" set "BAI2_DIR=%SCRIPT_DIR%DeepRL_AOS_Suitability"

set "BAI3_DIR=%SCRIPT_DIR%Bai_3_Cost_Benefit_Analysis"
if not exist "%BAI3_DIR%" set "BAI3_DIR=%SCRIPT_DIR%Cost_Benefit_Analysis"

echo ===============================================================================
echo            HE THONG DIEU PHOI THUC NGHIEM SONG SONG (BAI 2 VA BAI 3)
echo ===============================================================================
echo.
echo  [1] Chay SONG SONG Test Nhanh (Demo: 3 do thi, 1 seed) - Kiem tra he thong
echo  [2] Chay SONG SONG Nhom Type 1 (9 do thi, 20 seeds, 5 workers moi bai = 10 workers tong)
echo  [3] Chay SONG SONG Toan Bo (28 do thi, 20 seeds, 5 workers moi bai = 10 workers tong)
echo  [4] Tuy chon tham so (Custom Datasets / Seeds / Workers)
echo  [5] Thoat
echo.
echo ===============================================================================

set "choice="
set /p choice="Nhap lua chon cua ban (1-5): "

if "%choice%"=="1" goto opt1
if "%choice%"=="2" goto opt2
if "%choice%"=="3" goto opt3
if "%choice%"=="4" goto opt4
if "%choice%"=="5" goto end
goto invalid

:opt1
echo.
echo [*] Dang khoi chay 2 tien trinh song song o che do Demo Test...
start "BAI 2 - Deep RL AOS Suitability (Demo)" /D "%BAI2_DIR%" cmd /k ""%PYTHON_CMD%" run_bai2.py --datasets demo --seeds 1 --workers 2"
start "BAI 3 - Cost-Benefit Analysis (Demo)" /D "%BAI3_DIR%" cmd /k ""%PYTHON_CMD%" run_bai3.py --datasets demo --seeds 1 --workers 2"
echo [+] Da kich hoat 2 cua so thuc thi song song!
goto end

:opt2
echo.
echo [*] Dang khoi chay 2 tien trinh song song tren 9 mang Type 1 (20 seeds, tong 10 workers)...
start "BAI 2 - Deep RL AOS Suitability (Type 1)" /D "%BAI2_DIR%" cmd /k ""%PYTHON_CMD%" run_bai2.py --datasets Type1 --seeds 20 --workers 5"
start "BAI 3 - Cost-Benefit Analysis (Type 1)" /D "%BAI3_DIR%" cmd /k ""%PYTHON_CMD%" run_bai3.py --datasets Type1 --seeds 20 --workers 5"
echo [+] Da kich hoat 2 cua so thuc thi song song!
goto end

:opt3
echo.
echo [*] Dang khoi chay 2 tien trinh song song tren toan bo 28 mang (20 seeds, tong 10 workers)...
start "BAI 2 - Deep RL AOS Suitability (All 28)" /D "%BAI2_DIR%" cmd /k ""%PYTHON_CMD%" run_bai2.py --datasets all --seeds 20 --workers 5"
start "BAI 3 - Cost-Benefit Analysis (All 28)" /D "%BAI3_DIR%" cmd /k ""%PYTHON_CMD%" run_bai3.py --datasets all --seeds 20 --workers 5"
echo [+] Da kich hoat 2 cua so thuc thi song song!
goto end

:opt4
echo.
set "dset="
set /p dset="Chon tap du lieu (Type1 / Type2 / all / demo) [mac dinh Type1]: "
if "%dset%"=="" set "dset=Type1"
set "snum="
set /p snum="Nhap so luong seeds (vi du 20) [mac dinh 20]: "
if "%snum%"=="" set "snum=20"
set "wnum="
set /p wnum="Nhap so workers chay song song moi bai (mac dinh 5): "
if "%wnum%"=="" set "wnum=5"
echo.
echo [*] Dang khoi chay 2 tien trinh song song voi: Datasets=%dset%, Seeds=%snum%, Workers=%wnum% moi bai...
start "BAI 2 - Deep RL AOS Suitability" /D "%BAI2_DIR%" cmd /k ""%PYTHON_CMD%" run_bai2.py --datasets %dset% --seeds %snum% --workers %wnum%"
start "BAI 3 - Cost-Benefit Analysis" /D "%BAI3_DIR%" cmd /k ""%PYTHON_CMD%" run_bai3.py --datasets %dset% --seeds %snum% --workers %wnum%"
echo [+] Da kich hoat 2 cua so thuc thi song song!
goto end

:invalid
echo.
echo [!] Lua chon khong hop le.
pause
goto end

:end
echo.
echo ===============================================================================
echo Cac tien trinh da duoc khoi chay trong cua so doc lap.
echo Nhan phim bat ky de dong trinh dieu phoi...
pause >nul
