@echo off
setlocal
chcp 65001 >nul
title BAI 3 - COST-BENEFIT AND OVERHEAD ANALYSIS (10 WORKERS)

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

set "BAI3_DIR=%SCRIPT_DIR%Bai_3_Cost_Benefit_Analysis"
if not exist "%BAI3_DIR%" set "BAI3_DIR=%SCRIPT_DIR%Cost_Benefit_Analysis"

echo ===============================================================================
echo       CHUONG TRINH THUC NGHIEM BAI 3 (COST-BENEFIT AND OVERHEAD ANALYSIS)
echo ===============================================================================
echo.
echo  [1] Chay Test Nhanh (Demo: 3 do thi, 1 seed, 2 workers)
echo  [2] Chay Nhom Type 1 (9 do thi, 20 seeds, 10 workers song song)
echo  [3] Chay Toan Bo 28 do thi (28 do thi, 20 seeds, 10 workers song song)
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
echo [*] Dang khoi chay Bai 3 o che do Demo Test (2 workers)...
cd /d "%BAI3_DIR%"
"%PYTHON_CMD%" run_bai3.py --datasets demo --seeds 1 --workers 2
goto end

:opt2
echo.
echo [*] Dang khoi chay Bai 3 tren 9 mang Type 1 (20 seeds, 10 workers song song)...
cd /d "%BAI3_DIR%"
"%PYTHON_CMD%" run_bai3.py --datasets Type1 --seeds 20 --workers 10
goto end

:opt3
echo.
echo [*] Dang khoi chay Bai 3 tren toan bo 28 mang (20 seeds, 10 workers song song)...
cd /d "%BAI3_DIR%"
"%PYTHON_CMD%" run_bai3.py --datasets all --seeds 20 --workers 10
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
set /p wnum="Nhap so workers chay song song (mac dinh 10): "
if "%wnum%"=="" set "wnum=10"
echo.
echo [*] Dang khoi chay Bai 3 voi: Datasets=%dset%, Seeds=%snum%, Workers=%wnum%...
cd /d "%BAI3_DIR%"
"%PYTHON_CMD%" run_bai3.py --datasets %dset% --seeds %snum% --workers %wnum%
goto end

:invalid
echo.
echo [!] Lua chon khong hop le.
pause
goto end

:end
echo.
echo ===============================================================================
echo Thuc nghiem hoan tat hoac da dung. Nhan phim bat ky de thoat...
pause >nul
