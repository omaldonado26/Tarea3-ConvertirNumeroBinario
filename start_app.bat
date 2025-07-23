@echo off
REM -----------------------------
REM Arranca Django y abre navegador
REM -----------------------------
cd /d %~dp0

echo Activando entorno virtual...
call venv\Scripts\activate.bat

echo Aplicando migraciones...
python manage.py migrate

echo Abriendo navegador...
start "" "http://127.0.0.1:8000/"

echo Iniciando servidor de desarrollo...
python manage.py runserver
