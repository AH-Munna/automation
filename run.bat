@echo off
cd /d "%~dp0"
echo Current directory: %cd%
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found at venv\Scripts\activate.bat
    pause
    exit /b 1
)
echo Activating virtual environment...
call "venv\Scripts\activate.bat"
echo Running controller.py...
python "controller_app.py"
echo Script completed.