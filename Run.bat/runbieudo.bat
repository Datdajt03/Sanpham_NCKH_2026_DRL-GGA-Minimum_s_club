@echo off
setlocal
chcp 65001 >nul
title EVO-RL - Xuat Bieu Do Chuan Bao Cao (Chart_seed)
cls

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

echo ===============================================================================
echo       EVO-RL MSCC FRAMEWORK - TRINH XUAT BIEU DO TU DONG (CHART_SEED)
echo ===============================================================================
echo.
echo [*] Dang quet toan bo du lieu thuc nghiem trong thu muc 'results/'...
echo [*] Tu dong tao thu muc 'Chart_seed' va ket xuat cac bieu do phan tich 600 DPI va Vector PDF...
echo.

"%PYTHON_CMD%" "%SCRIPT_DIR%analysis\render_enhanced_charts.py" %*
set "CHART_EXIT_CODE=%ERRORLEVEL%"

echo.
if %CHART_EXIT_CODE% EQU 0 (
    echo ===============================================================================
    echo [V] DA XUAT TOAN BO BIEU DO THANH CONG!
    echo [*] Vui long kiem tra thu muc 'Chart_seed' ben trong cac folder con cua 'results/'.
    echo ===============================================================================
) else (
    echo ===============================================================================
    echo [!] CO LOI XAY RA TRONG QUA TRINH TAO BIEU DO.
    echo ===============================================================================
)

echo.
pause
