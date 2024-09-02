@echo off
setlocal enabledelayedexpansion

REM Load environment variables from .env file
if exist ".env" (
    for /f "tokens=* delims=" %%x in (.env) do (
        set "line=%%x"
        if not "!line!"=="" (
            set "varname=!line:~0,findstr.exe /b /e "delims==" "varname""
            if not "!varname!"=="" (
                for /f "tokens=1,2 delims==" %%a in ("!line!") do (
                    set "%%a=%%b"
                )
            )
        )
    )
)

REM Print the starting time
echo ---> Starting at: %DATE% %TIME%

REM Set defaults if the values are not provided
if "%PORT%"=="" set "PORT=5767"
if "%OPENAI_API_KEY%"=="" set "OPENAI_API_KEY=OPENAI_API_KEY value is not set in the Addon configuration"

REM Set FLASK_APP environment variable
set "FLASK_APP=app.py"

REM Activate the virtual environment
call venv\Scripts\activate

REM Run the Flask app with the specified port
python -m flask run --host=0.0.0.0 --port=%PORT%

REM Deactivate the virtual environment
deactivate

