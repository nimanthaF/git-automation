@echo off
cd G:\"python automation"\pyhton-automation
set /p name=enter the project name: 
python automation.py %name%
git add .
git commit -m "first commut"
git push
pause