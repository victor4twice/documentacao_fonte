@echo off
cd /d "%~dp0"
title Painel de Gravacoes

if not exist "server.py" (
  echo ERRO: server.py nao foi encontrado nesta pasta.
  echo Deixe o iniciar.bat, o server.py e o index.html juntos, na mesma pasta.
  echo Se os arquivos estao dentro de um .zip, extraia tudo antes.
  pause
  exit /b 1
)

py --version >nul 2>nul
if not errorlevel 1 (set "PY=py" & goto start)

python --version >nul 2>nul
if not errorlevel 1 (set "PY=python" & goto start)

echo Python nao encontrado neste computador.
echo Abrindo o painel direto no navegador (sem o servidor).
echo Neste modo, fontes novas devem ser adicionadas no arquivo fontes.js.
start "" "%~dp0index.html"
timeout /t 6 >nul
exit /b 0

:start
%PY% server.py
echo.
echo O servidor parou. Se apareceu algum erro acima, me envie a mensagem.
pause
