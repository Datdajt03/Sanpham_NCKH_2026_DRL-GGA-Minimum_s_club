@echo off
setlocal
chcp 65001 >nul
title EVO-RL MSCC - Cai Dat Moi Truong Tu Dong (1-Click Setup)

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

color 0B
cls
echo ===============================================================================
echo          HE THONG EVO-RL MSCC: THIET LAP MOI TRUONG TU DONG (1-CLICK SETUP)
echo ===============================================================================
echo  * De tai: Toi uu hoa Tien hoa ket hop Deep RL [PPO-AOS] cho Minimum s-Club Cover
echo  * Nen tang: Windows 10/11 x64 [CPU Da nhan + GPU NVIDIA Tensor Cores]
echo ===============================================================================
echo.

:: ===============================================================================
:: BUOC 1: KIEM TRA VA HOAN THIEN CAU TRUC THU MUC
:: ===============================================================================
echo [*] BUOC 1/5: Kiem tra va hoan thien cau truc thu muc du an...

if not exist "%SCRIPT_DIR%results" (
    mkdir "%SCRIPT_DIR%results" >nul 2>&1
    echo  [+] Da khoi tao thu muc ket qua: results
)

if exist "%SCRIPT_DIR%results" (
    echo  [+] Da xac nhan thu muc ket qua: results
)

if exist "%SCRIPT_DIR%pbodulieu" (
    echo  [+] Da xac nhan thu muc du lieu benchmark: pbodulieu
) else (
    echo  [!] Canh bao: Chua tim thay thu muc du lieu pbodulieu
)

echo  [V] Cau truc thu muc da hoan thien!
echo.

:: ===============================================================================
:: BUOC 2: TIM KIEM VA NHAN DIEN PYTHON
:: ===============================================================================
echo [*] BUOC 2/5: Dang quet tim moi truong Python tren he thong...

set "PYTHON_CMD="

if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    set "PYTHON_CMD=%SCRIPT_DIR%.venv\Scripts\python.exe"
    goto python_found
)
if exist "%~d0\conda\python.exe" (
    set "PYTHON_CMD=%~d0\conda\python.exe"
    goto python_found
)
if exist "A:\conda\python.exe" (
    set "PYTHON_CMD=A:\conda\python.exe"
    goto python_found
)
if exist "C:\conda\python.exe" (
    set "PYTHON_CMD=C:\conda\python.exe"
    goto python_found
)
if exist "D:\conda\python.exe" (
    set "PYTHON_CMD=D:\conda\python.exe"
    goto python_found
)
if exist "%USERPROFILE%\miniconda3\python.exe" (
    set "PYTHON_CMD=%USERPROFILE%\miniconda3\python.exe"
    goto python_found
)
if exist "%USERPROFILE%\anaconda3\python.exe" (
    set "PYTHON_CMD=%USERPROFILE%\anaconda3\python.exe"
    goto python_found
)
if exist "C:\ProgramData\anaconda3\python.exe" (
    set "PYTHON_CMD=C:\ProgramData\anaconda3\python.exe"
    goto python_found
)
if exist "C:\miniconda3\python.exe" (
    set "PYTHON_CMD=C:\miniconda3\python.exe"
    goto python_found
)
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
    goto python_found
)
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    goto python_found
)
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
    goto python_found
)
if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
    goto python_found
)
if exist "C:\Program Files\Python313\python.exe" (
    set "PYTHON_CMD=C:\Program Files\Python313\python.exe"
    goto python_found
)
if exist "C:\Program Files\Python312\python.exe" (
    set "PYTHON_CMD=C:\Program Files\Python312\python.exe"
    goto python_found
)
if exist "C:\Program Files\Python311\python.exe" (
    set "PYTHON_CMD=C:\Program Files\Python311\python.exe"
    goto python_found
)
if exist "C:\Program Files\Python310\python.exe" (
    set "PYTHON_CMD=C:\Program Files\Python310\python.exe"
    goto python_found
)

for /f "delims=" %%I in ('where python.exe 2^>nul') do (
    set "PYTHON_CMD=%%I"
    goto python_found
)

for /f "delims=" %%I in ('where py.exe 2^>nul') do (
    set "PYTHON_CMD=%%I"
    goto python_found
)

:: Khong tim thay Python
echo.
echo ===============================================================================
echo [X] KHONG TIM THAY PYTHON TREN MAY TINH CUA BAN!
echo ===============================================================================
echo He thong can Python 3.10 tro len de chay du an EVO-RL.
echo.

where winget >nul 2>&1
if %ERRORLEVEL% NEQ 0 goto manual_python

echo May tinh cua ban co san Windows Package Manager [winget].
choice /C YN /M ">> Ban co muon tu dong cai dat Python 3.11 qua winget khong" /T 15 /D Y
if errorlevel 2 goto manual_python
echo.
echo [*] Dang cai dat Python 3.11 qua winget...
winget install Python.Python.3.11 --silent --accept-package-agreements --accept-source-agreements
echo [*] Cai dat hoan tat. Vui long chay lai setup.bat!
pause
exit /b 0

:manual_python
echo.
echo [*] Vui long tai va cai dat Python 3.11 hoac 3.12 tai:
echo     https://www.python.org/downloads/
echo [*] LUU Y: Hay tich chon 'Add Python to PATH' khi cai dat!
echo.
pause
exit /b 1

:python_found
set "PYTHON_BASE=%PYTHON_CMD%"
echo  [+] Da tim thay Python: "%PYTHON_BASE%"
for /f "delims=" %%V in ('"%PYTHON_BASE%" --version 2^>^&1') do echo  [+] Phien ban: %%V
echo.

:: ===============================================================================
:: BUOC 3: CAU HINH MOI TRUONG THUC THI [.venv HOAC TRUC TIEP]
:: ===============================================================================
echo [*] BUOC 3/5: Thiet lap moi truong thuc thi...

if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" goto venv_exists

if /i "%~1"=="2" goto opt_direct
if /i "%~1"=="direct" goto opt_direct
if /i "%~1"=="1" goto opt_venv
if /i "%~1"=="venv" goto opt_venv

echo.
echo Lua chon cach thuc cai dat moi truong:
echo  [1] Khoi tao moi truong ao rieng biet [.venv] [Khuyen nghi]
echo  [2] Cai dat truc tiep vao Python hien tai
echo.
choice /C 12 /M ">> Nhap lua chon cua ban (1 hoac 2) [Mac dinh 1 sau 10s]: " /T 10 /D 1
if errorlevel 2 goto opt_direct
goto opt_venv

:venv_exists
echo  [+] Phat hien moi truong ao noi bo [.venv] da co san.
set "PYTHON_CMD=%SCRIPT_DIR%.venv\Scripts\python.exe"
goto setup_packages

:opt_direct
echo.
echo [*] Dang thiet lap cai dat truc tiep vao: "%PYTHON_BASE%"
set "PYTHON_CMD=%PYTHON_BASE%"
goto setup_packages

:opt_venv
echo.
echo [*] Dang khoi tao moi truong ao Python [.venv]...
"%PYTHON_BASE%" -m venv "%SCRIPT_DIR%.venv"
if exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    set "PYTHON_CMD=%SCRIPT_DIR%.venv\Scripts\python.exe"
    echo  [+] Da tao moi truong ao .venv thanh cong!
) else (
    echo  [*] Khoi tao .venv khong thanh cong, tiep tuc su dung Python hien tai.
    set "PYTHON_CMD=%PYTHON_BASE%"
)
goto setup_packages

:setup_packages
echo.
echo  [*] Trinh thong dich thuc thi: "%PYTHON_CMD%"
echo.

:: ===============================================================================
:: BUOC 4: NANG CAP PIP VA CAI DAT THU VIEN PHU THUOC
:: ===============================================================================
echo [*] BUOC 4/5: Dang tien hanh cai dat cac goi phu thuoc...
echo.

echo [*] [1/4] Nang cap cong cu quan ly goi pip...
"%PYTHON_CMD%" -m pip install --upgrade pip --quiet
echo  [+] Trinh quan ly goi pip da duoc cap nhat.
echo.

echo [*] [2/4] Kiem tra phan cung card do hoa NVIDIA CUDA...
where nvidia-smi >nul 2>&1
if %ERRORLEVEL% NEQ 0 goto no_gpu

echo  [+] Da phat hien card do hoa NVIDIA!
"%PYTHON_CMD%" -c "import torch; exit(0 if torch.cuda.is_available() else 1)" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo  [+] PyTorch voi bo tang toc CUDA da san sang.
    goto after_torch
)

echo  [*] Dang cai dat PyTorch ho tro GPU CUDA Tensor Cores...
"%PYTHON_CMD%" -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
if %ERRORLEVEL% EQU 0 goto after_torch

echo  [*] Thu lai cai dat PyTorch tieu chuan...
"%PYTHON_CMD%" -m pip install torch
goto after_torch

:no_gpu
echo  [*] Khong phat hien card do hoa NVIDIA. Su dung CPU da nhan.
"%PYTHON_CMD%" -c "import torch" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo  [*] Dang cai dat PyTorch CPU...
    "%PYTHON_CMD%" -m pip install torch
)

:after_torch
echo.
echo [*] [3/4] Cai dat cac thu vien tu requirements.txt...
"%PYTHON_CMD%" -m pip install -r "%SCRIPT_DIR%requirements.txt"
if %ERRORLEVEL% EQU 0 (
    echo  [+] Da cai dat xong requirements.txt.
) else (
    echo  [!] Co loi xay ra trong qua trinh cai requirements.txt.
)
echo.

echo [*] [4/4] Cai dat thu vien phan tich do thi igraph C-Core...
"%PYTHON_CMD%" -m pip install igraph --quiet
echo  [+] Thu vien igraph da san sang.
echo.

:: ===============================================================================
:: BUOC 5: TU KIEM TRA MOI TRUONG TOAN DIEN [SELF-TEST DIAGNOSTIC]
:: ===============================================================================
echo [*] BUOC 5/5: Dang chay quy trinh tu chan doan moi truong...
echo.

"%PYTHON_CMD%" "%SCRIPT_DIR%check_env.py"
if %ERRORLEVEL% NEQ 0 goto test_failed

echo.
echo ===============================================================================
echo  [V] HOAN TAT CAI DAT MOI TRUONG THANH CONG 100%%!
echo ===============================================================================
echo  Toan bo he sinh thai thuc nghiem EVO-RL da san sang hoat dong:
echo   - CHAY_CHUONG_TRINH_TONG.bat: Chuong trinh Tong quan ly tat ca tinh nang (Khuyen nghi)
echo   - setup.bat                 : Cai dat va cau hinh moi truong tu dong
echo   - Run.bat\                  : Thu muc chua toan bo runner thuc nghiem chi tiet:
echo       * run.bat               : Thuc nghiem EVO-RL MSCC (Tuy chon do thi ^& sieu tham so)
echo       * runbieudo.bat         : Xuat bieu do phan tich ^& hoi tu (600 DPI)
echo       * run_tong_hop_so_lieu.bat : Tong hop so lieu phan tich toan dien
echo       * verify_all.bat        : Kiem tra xac thuc 9 giai doan he thong
echo ===============================================================================
echo.

if /i "%~1"=="--no-launch" goto finish
if /i "%~2"=="--no-launch" goto finish

choice /C YN /M ">> Ban co muon KHOI CHAY NGAY Chuong trinh Tong khong? (Y/N)" /T 15 /D Y
if errorlevel 2 goto finish
if errorlevel 1 (
    echo.
    echo [*] Dang khoi chay CHAY_CHUONG_TRINH_TONG.bat...
    call "%SCRIPT_DIR%CHAY_CHUONG_TRINH_TONG.bat"
    goto finish
)

:test_failed
echo.
echo ===============================================================================
echo [X] CANH BAO: Kiem tra phat hien moi truong chua day du hoac co loi.
echo [*] Vui long xem thong bao chi tiet o tren de khac phuc.
echo ===============================================================================
echo.
goto finish

:finish
echo.
echo [*] Phien cai dat hoan tat.
if /i not "%~1"=="--no-launch" if /i not "%~2"=="--no-launch" (
    echo Nhan phim bat ky de dong cua so.
    pause >nul
)
