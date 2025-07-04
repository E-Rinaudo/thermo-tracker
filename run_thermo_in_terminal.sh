#!/bin/bash

VENV_PATH="/Users/enricorinaudo/Desktop/Coding/python_work/my_projects/thermo_tracker/venv"
SCRIPT_PATH="/Users/enricorinaudo/Desktop/Coding/python_work/my_projects/thermo_tracker/thermo_tracker.py"

osascript -e 'tell application "Terminal"
    activate
    do script "'"$VENV_PATH"'/bin/python '"$SCRIPT_PATH"'"
end tell'
