@echo off
set app=Main
set icon=icon
cd /d %~dp0
pyinstaller --onefile --icon=%icon%.ico %app%.py