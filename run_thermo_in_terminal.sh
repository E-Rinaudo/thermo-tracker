#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_PATH="$PROJECT_DIR/venv"
SCRIPT_PATH="$PROJECT_DIR/thermo_tracker.py"

osascript -e 'tell application "Terminal"
    activate
    do script "'"$VENV_PATH"'/bin/python '"$SCRIPT_PATH"'"
end tell'
