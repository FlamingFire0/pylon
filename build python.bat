@echo off
set app=main
set icon=icon
cd /d %~dp0
pyinstaller --onefile --icon=%icon%.ico %app%.py