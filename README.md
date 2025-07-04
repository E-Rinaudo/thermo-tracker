# Thermo Tracker

[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Thermo Tracker** is a terminal-based Python application for tracking radiator heat usage.
It helps record, calculate, and organize heat consumption data from radiators equipped with ISTA heat cost allocators.

---

## Table of Contents

- [Thermo Tracker](#thermo-tracker)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Run the App](#run-the-app)
  - [Usage](#usage)
    - [Sample Output](#sample-output)
    - [Code Example](#code-example)
  - [License](#license)
  - [Contact](#contact)

---

## About

This project was originally created for personal use, but may be useful to others with similar needs.
It guides the user through setting up a data folder, registering the radiators, and entering readings.  
All data is saved in Excel files for easy review and future reference.

[back to top](#thermo-tracker)

---

## Features

- Guided setup for data folder and configuration.
- Radiator details (name, ID, coefficient) are stored in a registry file and can be updated as needed.
- Preferences (like date format and input mode) are saved and loaded automatically from a configuration file.
- Valve setting and raw reading input for each radiator.
- Automatic calculation of actual heat usage.
- Notes section for each data entry session.
- Data saved in Excel files.
- Cross-platform (macOS, Windows, Linux).

Main Excel file where data is stored, follows this format:

| Date     | Radiator Name | Radiator ID | Coefficient | Raw Reading | Actual Value | Total | Valve Setting | Notes |
|----------|---------------|-------------|-------------|-------------|--------------|-------|---------------|-------|
| 01/04/25 | Kitchen       | 0           | 1           | 10          | 10           |       | 2             |       |
| 01/04/25 | Living Room   | 1           | 2           | 7           | 14           |       | 2.5           |       |
| 01/04/25 | Gym           | 2           | 3           | 15          | 45           |       | 3             |       |
| 01/04/25 |               |             |             |             |              | 69    |               |       |

[back to top](#thermo-tracker)

---

## Built With

- [![Python][Python-badge]][Python-url]
- [![Visual Studio Code][VSCode-badge]][VSCode-url]
- [![Openpyxl][Openpyxl-badge]][Openpyxl-url]
- [![PyInputPlus][PyInputPlus-badge]][PyInputPlus-url]
- [![Mypy][Mypy-badge]][Mypy-url]
- [![Black][Black-badge]][Black-url]
- [![Docformatter][Docformatter-badge]][Docformatter-url]
- [![Pylint][Pylint-badge]][Pylint-url]
- [![Flake8][Flake8-badge]][Flake8-url]
- [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#thermo-tracker)

---

## Getting Started

### Prerequisites

- [Python][Python-download]
- [Git][Git-download]
  
### Setup

```bash
# Clone the repository
git clone https://github.com/E-Rinaudo/thermo_tracker.git # Using Git
gh repo clone E-Rinaudo/thermo_tracker # Using GitHub CLI

# Create a virtual environment
cd thermo_tracker
python -m venv venv

# Activate the virtual environment (all platforms)
source venv/bin/activate # On macOS/Linux
venv\Scripts\activate # On Windows
.\venv\Scripts\activate.bat # On Windows with CMD
.\venv\Scripts\activate.ps1 # On Windows with PowerShell
source venv/Scripts/activate # On Windows with Unix-like shells (e.g. Git Bash)

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
python thermo_tracker.py
```

Or, on macOS, use the provided shell script to launch in a new Terminal window:

```bash
./run_thermo_in_terminal.sh # This script can also be used with Platypus to create a standalone macOS app bundle. https://sveinbjorn.org/platypus
```

[back to top](#thermo-tracker)

---

## Usage

- On first launch, follow the prompts to set up your data folder.
- Enter radiator details (name, ID, coefficient) when prompted.
- Configure your usage file (years, date format, date input mode).
- Enter valve settings and raw reading for each radiator.
- Optionally, add notes for the session.
- Data is saved in Excel files for future review.

### Sample Output

```text
                    USAGE FILE CREATION

1. You'll enter the years to include in the file name.
   If you choose different years in future runs, a new file will be created,
   allowing you to keep data for each heating season separate.

2. You'll choose the date format for recording when readings are taken:
   - DD/MM/YYYY (European format)
   - MM/DD/YYYY (American format)

3. You'll also decide whether to insert the dates manually or automatically.
   Manual input can be used if you want to record a date different from the current date
   (e.g., if you took readings yesterday but are entering them today).

These three settings can be adjusted every time you run the program.

4. For each radiator, you'll enter the valve setting, which is the position
   or number set on the radiator valve.
   Then, you'll enter the raw reading from the HCA device.
   The program will calculate actual heat usage for each radiator.

5. Optionally, you can add any notes about that day's readings.
   This section is for general comments or observations about the
   data entry session.
```

### Code Example

An example from `thermo_tracker.py` showing the main workflow:

```py
class ThermoTracker:
    def run_app(self) -> None:
        """Runs the main process to configure and generate required files."""
        logging.debug("Starting the program.")
        utils.display_user_info(UserMsgs.INTRO.value)

        self._get_config_manager().open_config()

        folder = self._get_folder_manager()
        folder.update_folder_path()
        folder.handle_folder_selection()

        registry = self._get_registry_manager()
        registry.update_registry_path()
        registry.setup_registry()

        usage = self._get_usage_manager()
        usage.update_usage_path()
        usage.setup_usage()
```

[back to top](#thermo-tracker)

---

## License

Distributed under the MIT License. See [`LICENSE.txt`](LICENSE.txt) for details.

[back to top](#thermo-tracker)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email. Your feedback is appreciated as it helps me to continue improving.

- Email: <enricorinaudo91@gmail.com>  

You can also explore my GitHub profile.

- GitHub: [E-Rinaudo](https://github.com/E-Rinaudo)

[back to top](#thermo-tracker)

---

**Happy coding!**

<!-- SHIELDS -->
[stars-shield]: https://img.shields.io/github/stars/E-Rinaudo/thermo_tracker.svg?style=flat
[stars-url]: https://github.com/E-Rinaudo/thermo-tracker/stargazers
[license-shield]: https://img.shields.io/github/license/E-Rinaudo/thermo_tracker.svg?style=flat
[license-url]: https://github.com/E-Rinaudo/thermo-tracker/blob/main/LICENSE.txt
[Gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white
[Gmail-url]: mailto:enricorinaudo91@gmail.com

<!-- BADGES -->
[Python-badge]: https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54&style=flat
[Python-url]: https://docs.python.org/3/
[VSCode-badge]: https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=fff&style=flat
[VSCode-url]: https://code.visualstudio.com/docs
[Openpyxl-badge]: https://img.shields.io/badge/openpyxl-darkgreen?logo=python&logoColor=ffdd54&style=flat
[Openpyxl-url]: https://openpyxl.readthedocs.io/en/stable/
[PyInputPlus-badge]:https://img.shields.io/badge/PyInputPlus-4caf50?logo=python&logoColor=ffdd54&style=flat
[PyInputPlus-url]: https://pyinputplus.readthedocs.io/en/latest/
[Mypy-badge]: https://img.shields.io/badge/mypy-checked-blue?style=flat
[Mypy-url]: https://mypy.readthedocs.io/
[Black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[Black-url]: https://black.readthedocs.io/en/stable/
[Pylint-badge]: https://img.shields.io/badge/linting-pylint-yellowgreen?style=flat
[Pylint-url]: https://pylint.readthedocs.io/
[Ruff-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[Ruff-url]: https://docs.astral.sh/ruff/tutorial/
[Flake8-badge]: https://img.shields.io/badge/linting-flake8-blue?style=flat
[Flake8-url]: https://flake8.pycqa.org/en/latest/
[Docformatter-badge]: https://img.shields.io/badge/formatter-docformatter-fedcba.svg
[Docformatter-url]: https://github.com/PyCQA/docformatter

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
