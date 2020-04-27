@echo off
cd G:\"python automation"\pyhton-automation
set /p name=enter the project name: 
python automation.py %name%
cd G:\"automation test"
git clone https://github.com/nimanthaF/%name%.git
cd G:\"automation test"\%name%
git add .
git commit -m "first commit"
git push 
pause