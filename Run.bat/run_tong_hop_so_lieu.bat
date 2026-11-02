@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title Tong Hop So Lieu Phan Tich Toan Dien

echo ===============================================================================
echo   TONG HOP VA DONG GOI SO LIEU PHAN TICH TOAN DIEN (EVO-RL MSCC)
echo   (Tap phu ^|C^|, Thoi gian chay, So lan danh gia N_evals, Kiem dinh Wilcoxon)
echo   Doc du lieu thuc nghiem 30 do thi benchmark tu thu muc: results/
echo ===============================================================================
echo.

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

echo [*] Dang tong hop du lieu tu thu muc results/ va dong goi theo thoi gian...
"%PYTHON_CMD%" "%SCRIPT_DIR%Tong_hop_so_lieu_phan_bien\extract_and_consolidate.py" %*
set "EXTRACT_EXIT_CODE=%ERRORLEVEL%"

echo.
if %EXTRACT_EXIT_CODE% EQU 0 (
    echo [OK] Da hoan tat xuat bao cao tong va toan bo file MD cho tung do thi!
    if exist "%SCRIPT_DIR%Tong_hop_so_lieu_phan_bien\LATEST_RUN_PATH.txt" (
        set /p LATEST_DIR=<"%SCRIPT_DIR%Tong_hop_so_lieu_phan_bien\LATEST_RUN_PATH.txt"
        echo [*] Thu muc ket qua moi nhat vua tao:
        echo     !LATEST_DIR!
    )
) else (
    echo [!] Da xay ra loi trong qua trinh xu ly. Vui long kiem tra lai moi truong Python.
)

echo.
pause
