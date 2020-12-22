@echo off
pip install pygame
pip install flask
pip install neat-python
pip install pickle
start http://localhost:5000
cd Games
cmd /k "flask run"
pause