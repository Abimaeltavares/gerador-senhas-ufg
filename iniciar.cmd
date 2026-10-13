@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    echo Ambiente virtual nao encontrado. Consulte o README para instalar.
    exit /b 1
)
if "%~1"=="" (
    ".venv\Scripts\python.exe" main.py --help
    exit /b
)
".venv\Scripts\python.exe" main.py %*
