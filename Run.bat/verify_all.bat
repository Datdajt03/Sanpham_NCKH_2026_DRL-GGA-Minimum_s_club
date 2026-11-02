@echo off
setlocal
chcp 65001 >nul
title EVO-RL - Council Verification (9 Stages)

set "RUN_DIR=%~dp0"
cd /d "%RUN_DIR%.."
set "SCRIPT_DIR=%CD%\"

color 0A
cls

echo ===============================================================================
echo       KIEM TRA VA XAC THUC TOAN DIEN HE THONG EVO-RL MSCC (1-CLICK VERIFY)
echo ===============================================================================
echo  * Muc tieu: Kiem chung 9 giai doan doc lap truoc khi nop Hoi dong Khoa hoc
echo  * Pham vi: Phan cung, Thu vien, Du lieu 30 do thi, Toan tu, PPO, Thuc nghiem
echo ===============================================================================
echo.

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

echo [*] Trinh thong dich Python: "%PYTHON_CMD%"
echo.

"%PYTHON_CMD%" "%SCRIPT_DIR%verify_system.py"
set "VERIFY_EXIT_CODE=%ERRORLEVEL%"

echo.
if %VERIFY_EXIT_CODE% EQU 0 (
    echo ===============================================================================
    echo [V] XAC THUC THANH CONG: Toan bo 9/9 giai doan deu dat chuan!
    echo [*] Goi san pham Sanpham_nckh hoan toan san sang ban giao cho Hoi dong.
    echo ===============================================================================
) else (
    echo ===============================================================================
    echo [X] CANH BAO: Phat hien loi kiem chung. Vui long ra soat log chi tiet phia tren.
    echo ===============================================================================
)

echo.
pause
