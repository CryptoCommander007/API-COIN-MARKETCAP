@echo off
:: Nombre del ambiente virtual
set VENV_DIR=venv

:: Verifica si pip está instalado
python -m pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Pip no está instalado. Por favor, instala pip y vuelve a intentar.
    exit /b 1
)

:: Verifica si virtualenv está instalado, si no, lo instala
python -m pip show virtualenv >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Instalando virtualenv...
    python -m pip install --user virtualenv
) ELSE (
    echo Virtualenv ya está instalado. Actualizando virtualenv...
    python -m pip install --upgrade virtualenv
)

:: Crear el ambiente virtual si no existe
IF NOT EXIST %VENV_DIR% (
    echo Creando ambiente virtual...
    python -m virtualenv %VENV_DIR%
) ELSE (
    echo El ambiente virtual ya existe.
)

:: Activar el ambiente virtual
echo Activando el ambiente virtual...
call %VENV_DIR%\Scripts\activate

:: Pausa para mantener la ventana abierta
echo Ambiente virtual activado. Presiona cualquier tecla para continuar...
pause
