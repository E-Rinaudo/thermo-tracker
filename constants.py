#!/usr/bin/env python3


# region Module Description And Imports.
"""Constants and configuration values for the Thermo Tracker program.

This module stores fixed constants to avoid hardcoding them throughout
the project.
"""

import os
from enum import Enum, StrEnum, IntEnum
from textwrap import dedent

# endregion.


# region Constants.


class Folders(StrEnum):
    """Enum storing folder paths.

    Attributes:
        DEFAULT_EXCEL_FOLDER (str): Default path for saving Excel files.
        CONFIG_FOLDER (str): Hidden folder storing the JSON configuration file.
        USAGE_FOLDER (str): Default name for the subfolder in the Excel folder
            for usage files.
        FOLDER_NAME_SUFFIX (str): Suffix appended to the Excel folder name to
            ensure uniqueness when creating a new setup.
    """

    DEFAULT_EXCEL_FOLDER = os.path.join(os.path.expanduser("~"), "Desktop", "thermo_tracker")
    CONFIG_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".thermo_tracker")
    USAGE_FOLDER = "radiators_usage"
    FOLDER_NAME_SUFFIX = "_new"


class Files(StrEnum):
    """Enum defining labels for files in Thermo Tracker.

    Attributes:
        LOG_FILE (str): Path to the logging file.
        CONFIG_FILE (str): Full path to the JSON config file containing
            saved settings.
        RADIATORS_REGISTRY (str): Excel file name for static radiator data
            (Name, ID, Coefficient).
        DEFAULT_USAGE_NAME (str): Default name for the Excel usage data file.
        YEARS_PLACEHOLDER (str): Placeholder used in the usage filename
            for the years.
        XLSX (str): Pattern for matching Excel files.
    """

    LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_file.txt")
    CONFIG_FILE = os.path.join(Folders.CONFIG_FOLDER, "thermo_tracker_config.json")
    RADIATORS_REGISTRY = "radiators_registry.xlsx"
    DEFAULT_USAGE_NAME = "radiators_usage_[Years].xlsx"
    YEARS_PLACEHOLDER = "[Years]"
    XLSX = "*.xlsx"


class ConfigKeys(StrEnum):
    """Enum for keys used to retrieve values from the config file.

    Attributes:
        EXCEL_FOLDER (str): To retrieve the Excel folder path.
        REGISTRY_FILE (str): To retrieve the registry file path.
        RADIATORS_OWNED (str): To retrieve the number of owned radiators.
        USAGE_FOLDER_PATH (str): To retrieve the usage files folder path.
        USAGE_NAME (str): To retrieve the file name of the current usage file.
        DATE_FORMAT (str): To retrieve the preferred date format (EU or US).
        DATE_INPUT_MODE (str): To retrieve the date input mode (manual or auto).
        LAST_START_ROW (str): The row index where the previous run's data block
            began.
        START_ROW (str): The row index in the usage Excel file where the current
            radiator data block begins. Used to align new data entries.
    """

    EXCEL_FOLDER = "excel_folder"
    REGISTRY_FILE = "registry_file"
    RADIATORS_OWNED = "radiators_owned"
    USAGE_FOLDER_PATH = "usage_folder_path"
    USAGE_NAME = "usage_name"
    DATE_FORMAT = "date_format"
    DATE_INPUT_MODE = "date_input_mode"
    LAST_START_ROW = "last_start_row"
    START_ROW = "start_row"


class DateFormats(StrEnum):
    """Enum defining supported date formats for the usage file.

    Attributes:
        EU_FORMAT (str): European format string (DD/MM/YYYY).
        US_FORMAT (str): U.S. format string (MM/DD/YYYY).
        EU_LABEL (str): Readable label for the European date format.
        US_LABEL (str): Readable label for the U.S. date format.
    """

    EU_FORMAT = "%d/%m/%Y"
    US_FORMAT = "%m/%d/%Y"
    EU_LABEL = "DD/MM/YYYY"
    US_LABEL = "MM/DD/YYYY"


class CalendarLimits(IntEnum):
    """Enum defining boundaries related to calendar dates.

    Attributes:
        MIN_DAYS (int): Lowest number of days in any month.
        MIN_MONTHS (int): Lowest number of months in a year.
        MAX_DAYS (int): Maximum number of days in any month.
        MAX_MONTHS (int): Total number of months in a year.
    """

    MIN_DAYS = 1
    MIN_MONTHS = 1
    MAX_DAYS = 31
    MAX_MONTHS = 12


class SharedConstants(StrEnum):
    """Enum for shared constants used across the application.

    Attributes:
        AGREE (str): Standard affirmative response ("yes").
        UPDATE (str): Key used to track if configuration updates are needed.
        DATE_AUTO (str): Value for automatic date input mode.
        DATE_MANUAL (str): Value for manual date input mode.
        EUROPEAN (str): String identifier for the European date format.
        AMERICAN (str): String identifier for the American date format.
        EMPTY_STR (str): Value for an empty string.
    """

    AGREE = "yes"
    UPDATE = "UPDATE"
    DATE_AUTO = "Auto"
    DATE_MANUAL = "Manual"
    EUROPEAN = "European"
    AMERICAN = "American"
    EMPTY_STR = ""


class RegexPatterns(StrEnum):
    """Regex patterns used for validating user input in usage_manager.

    Attributes:
       YEARS (str): Regex pattern to validate the date for the usage file name
            (e.g., "2025-2026").
       DATE_REGEX (str): Regex pattern to validate date format input
           (e.g., "European" or "American").
       DATE_INPUT_REGEX (str): Regex pattern to validate date input mode
           (e.g., "Auto" or "Manual").
       BLOCK (str): Regex pattern used in pyinputplus to block unwanted inputs.
    """

    YEARS = r"^\d{4}-\d{4}$"
    DATE_REGEX = rf"^({SharedConstants.EUROPEAN}|{SharedConstants.AMERICAN})$"
    DATE_INPUT_REGEX = rf"^({SharedConstants.DATE_AUTO}|{SharedConstants.DATE_MANUAL})$"
    BLOCK = r".*"


class ThermoInstances(StrEnum):
    """Enum for keys used to access instances in ThermoTracker.

    These keys are used in the ThermoTracker.instances dictionary to retrieve
    specific manager instances.

    Attributes:
        CONFIG (str): Key for the ConfigManager instance.
        FOLDER (str): Key for the ExcelFolderManager instance.
        REGISTRY (str): Key for the RegistryManager instance.
        USAGE (str): Key for the UsageManager instance.
    """

    CONFIG = "CONFIG"
    FOLDER = "FOLDER"
    REGISTRY = "REGISTRY"
    USAGE = "USAGE"


class Labels(StrEnum):
    """Enum for labels used in logging and printing.

    Attributes:
        REGISTRY (str): Label for registry-related files and logs.
        USAGE (str): Label for usage-related files and logs.
    """

    REGISTRY = "registry"
    USAGE = "usage"


class ManagerIdentifiers(StrEnum):
    """Enum for keys used to access instances in Excel manager classes.

    Attributes:
        REGISTRY_GENERATOR (str): Key for the RegistryGenerator instance
            in RegistryManager.
        REGISTRY_UPDATER (str): Key for the RegistryUpdater instance
            in RegistryManager.
        USAGE_CONFIG (str): Key for the UsageConfigurator instance
            in UsageManager.
        USAGE_GENERATOR (str): Key for the UsageGenerator instance
            in UsageManager.
    """

    REGISTRY_GENERATOR = "REGISTRY_GENERATOR"
    REGISTRY_UPDATER = "REGISTRY_UPDATER"
    USAGE_CONFIG = "USAGE_CONFIG"
    USAGE_GENERATOR = "USAGE_GENERATOR"


class RegistryExcelMeta(Enum):
    """Enum for metadata for the radiators registry Excel sheet.

    Attributes:
        SHEET_NAME (str): Sheet name for the radiators registry file.
        HEADERS (tuple[str]): Column headers for the registry sheet.
        FREEZE_HEADERS (str): Cell reference for freezing panes in the sheet.
        COLS (tuple[str]): Column letters for the registry sheet.
        COL_EXTRA_SPACE (int): Extra space in the columns to improve visibility.
        FIRST_DATA_ROW (int): The first non header row in the registry file.
        RADIATOR_ROW (int): The row containing the name of each radiator.
    """

    SHEET_NAME = "Static Data"
    HEADERS = ("Radiator Name", "Radiator ID", "Coefficient")
    FREEZE_HEADERS = "A2"
    COLS = ("A", "B", "C")
    COL_EXTRA_SPACE = 5
    FIRST_DATA_ROW = 2
    RAD_NAME_ROW = 0


class UsageExcelMeta(Enum):
    """Enum for metadata for the radiators usage Excel sheet.

    Attributes:
        SHEET_NAME (str): Sheet name for the radiators usage file.
        HEADERS (tuple[str]): Column headers for the usage sheet.
        FREEZE_HEADERS (str): Cell reference for freezing panes in the sheet.
        COLS (tuple): Column letters for the usage sheet.
        COL_EXTRA_SPACE (int): Extra space in the columns to improve visibility.
        NOTES_COLUMN_SPACE (int): Extra space in the Notes column to improve
            visibility.
        NOTE_VERTICAL_ALIGNMENT (str): Vertical alignment for the note cell
            in the usage sheet.
        NOTE_HORIZONTAL_ALIGNMENT (str): Horizontal alignment for the note cell
            in the usage sheet.
        VS_NOTES_START_ROW (int): The row in which to write the valve setting
            note.
        BLANK_LINES (int): Extra three lines at the end of the radiator's block.
    """

    SHEET_NAME = "Radiators Usage"
    HEADERS = (
        "Date",
        "Radiator Name",
        "Radiator ID",
        "Coefficient",
        "Raw Reading",
        "Actual Value",
        "Total",
        "Valve Setting",
        "Notes",
    )
    FREEZE_HEADERS = "A2"
    COLS = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
    COL_EXTRA_SPACE = 10
    NOTES_COLUMN_SPACE = 50
    NOTE_VERTICAL_ALIGNMENT = "top"
    NOTE_HORIZONTAL_ALIGNMENT = "left"
    VS_NOTE_START_ROW = 1
    BLANK_LINES = 3


class UsageFileCols(IntEnum):
    """Enum storing the column indexes (1-based) for the Usage Excel sheet.

    Attributes:
        DATE (int): Column index for the date column.
        NAME (int): Column index for the radiator name column.
        COEFFICIENT (int): Column index for the coefficient column.
        RAW_READING (int): Column index for the raw reading column.
        ACTUAL_VALUE (int): Column index for the actual value column.
        TOTAL (int): Column index for the total column.
        VALVE_SETTING (int): Column index for the valve setting column.
        NOTES (int): Column index for the notes column.
    """

    DATE = 1
    NAME = 2
    COEFFICIENT = 4
    RAW_READING = 5
    ACTUAL_VALUE = 6
    TOTAL = 7
    VALVE_SETTING = 8
    NOTES = 9


class OsPlatforms(StrEnum):
    """Enum for OS platform identifiers and open commands.

    Used to determine the current OS and the appropriate command to open files.

    Attributes:
        MACOS (str): Value for the MacOS system.
        WINDOWS (str): Value for the Windows system.
        LINUX (str): Value for the Linux system.
        MACOS_OPEN (str): Command to open a file in MacOS.
        WINDOWS_OPEN (str): Command to open a file in Windows.
        LINUX_OPEN (str): Command to open a file in Linux.
    """

    MACOS = "darwin"
    WINDOWS = "win"
    LINUX = "linux"
    MACOS_OPEN = "open"
    WINDOWS_OPEN = "start"
    LINUX_OPEN = "xdg-open"


class UserMessages(StrEnum):
    """Enum for static user-facing messages and prompts.

    Attributes:
        INTRO (str): Explains the purpose and workflow of the program.
        FOLDER_GENERATION (str): Explains the folder management process.
        FOLDER_RESET_PROMPT (str): Advises the user to create a new folder
            if they have moved or changed the number of radiators.
        EXCEL_FOLDER_PROMPT (str): Asks for the path for saving Excel files.
        SAME_FOLDER_NAME (str): Informs the user that the selected folder
            matches the previous one. A suffix is added to ensure uniqueness.
        OLD_FILES_INFO (str): Informs about the option to migrate files.
        COPY_OLD_FILES (str): Asks to copy files from the old to the new folder.
        REGISTRY_GENERATION (str): Explains how to create the radiator registry.
        REGISTRY_UPDATE_RECAP (str): Asks if the registry needs updates.
        REGISTRY_UPDATE_DESCRIPTION (str): Explains how to update the registry.
        USAGE_GENERATION (str): Explains how to create the radiators usage file.
        YEARS_FILENAME_ENTRY (str): Asks to enter the years for the usage file.
        PROMPT_DATE_FORMAT (str): Asks to enter the date format
            (European or American).
        PROMPT_DATE_INPUT_MODE (str): Asks to enter the date input mode
            (Auto or Manual).
        USAGE_DATA_ENTRY_INTRO (str): Gives information about which data will
            the user be required to enter in the usage file.
        ENTER_MANUAL_DATE (str): Asks to provide the date for the radiators
            block.
        ENTER_RAW_READINGS (str): Asks to provide the raw readings for
            each radiator.
        VALVE_SETTING_ENTRY (str); Explains how to enter the valve settings.
        VALVE_SETTING_UPDATE (str): Explains how to update the valve settings.
        PROMPT_VALVE_UPDATE (str): Asks to update  the current valve setting.
        CHANGE_USAGE_CONFIG (str): Prompts to modify the current usage file
            configurations (file name, date format, date input mode).
        OPEN_USAGE (str): Asks whether to open the newly saved usage file.
    """

    INTRO = dedent(
        f"""
                                  THERMO TRACKER

    This App helps you track radiator heat usage.
    It records and calculates data from ISTA heat cost allocators.

                                ### How It Works ###:

    1. Choose a directory where to save your data.

    The program will create a folder, later filled with the following:

    - **{Files.RADIATORS_REGISTRY}**: Stores radiator details (Names, IDs, and Coefficients).
    - **{Folders.USAGE_FOLDER}**: Subfolder for radiator usage files created over the years.

    Inside the {Folders.USAGE_FOLDER}, you will find:

    - **{Files.DEFAULT_USAGE_NAME}**: Main file where data is stored, following this format:

    | Date     | Radiator Name | Radiator ID | Coefficient | Raw Reading | Actual Value | Total | Valve Setting | Notes |
    |----------|---------------|-------------|-------------|-------------|--------------|-------|---------------|-------|
    | 01/04/25 | Kitchen       | 0           | 1           | 10          | 10           |       | 2             |       |
    | 01/04/25 | Living Room   | 1           | 2           | 7           | 14           |       | 2.5           |       |
    | 01/04/25 | Gym           | 2           | 3           | 15          | 45           |       | 3             |       |
    | 01/04/25 |               |             |             |             |              | 69    |               |       |

    2. Enter radiator details (Name, ID, Coefficient).
       They will be saved in {Files.RADIATORS_REGISTRY} for future use.

    3. Configure your usage file by specifying:
       - The years to include in the {Files.DEFAULT_USAGE_NAME}.
       - The date format for recording readings.
       - Whether to input dates manually or automatically.

    4. Input valve setting and raw reading for each radiator.
       The program will calculate the actual heat usage for each radiator using the formula:
       Actual Value = Raw Reading * Coefficient

    5. Optionally, add any notes about that day's readings.
       This section is for general comments or observations about the data entry session,
       not specific to a single radiator.

    6. Your data is automatically saved and can be reviewed in {Files.DEFAULT_USAGE_NAME}.

    **IMPORTANT**
    If you move to a new home or change the number of radiators,
    please create a new folder and start a new setup.
    Do **not** reuse the old folder, as this may cause data inconsistencies.

    Press **Enter** to continue..."""
    )

    FOLDER_GENERATION = dedent(
        """
                    EXCEL FOLDER GENERATION

    The default folder path for saving Excel files is {folder_path}.

    You can choose to use this default folder or specify a custom folder.
    If you select a custom folder, the program will handle its creation
    and optionally migrate existing files.

    Shall we proceed with a custom folder instead of the default? (yes/no)
    """
    )

    FOLDER_RESET_PROMPT = dedent(
        """
                    NEED A NEW FOLDER

    An Excel folder already exists from a previous run:
    - {folder_path}.

    If you have moved or changed the number of radiators, it is recommended to create
    a new folder.

    Would you like to start the process of creating a new folder and starting
    a new setup, or continue adding data to the current folder?
    Type 'yes' to start over, or 'no' to keep the current setup.
    """
    )

    EXCEL_FOLDER_PROMPT = dedent(
        """
                    PROVIDE CUSTOM FOLDER

    Enter the full path, including the folder name, where files should be saved.
    Example: /Users/your_username/Desktop/folder_name(e.g. Thermo Tracker)
    """
    )

    SAME_FOLDER_NAME = dedent(
        """
                    NEW FOLDER NAME = OLD FOLDER NAME

    Selected folder is the same as the old folder:

    - New folder: {new_folder}
    - Old folder: {old_folder}

    Appending a suffix to create a unique folder name.

    Press **Enter** to continue..."""
    )

    OLD_FILES_INFO = dedent(
        """
                    MIGRATE OLD FILES

    You have configured a new folder for saving your files.

    Existing files in the old folder can be moved to the new folder.
    Below is a summary of the old folder's contents to help you decide.

    Press **Enter** to continue...
    """
    )

    COPY_OLD_FILES = dedent(
        """
    Copy existing files to the new folder? (yes/no)

    - Old Folder: {old_path}
    - New Folder: {new_path}

    Note: Files won't be deleted from the old folder.
    """
    )

    REGISTRY_GENERATION = dedent(
        f"""
                    RADIATORS REGISTRY GENERATION

    We are now going to create the file {Files.RADIATORS_REGISTRY}.

    You will first be asked how many radiators you own.

    Then, for each radiator, you will need to provide:

    - {RegistryExcelMeta.HEADERS.value[0]}: Short name for the radiator (e.g. Kitchen, Living Room).
    - {RegistryExcelMeta.HEADERS.value[1]}: Unique number for each radiator (e.g. 302030).
    - {RegistryExcelMeta.HEADERS.value[2]}: Number used to convert raw readings (e.g. 0.5, 1, 1.5).

    Note:
    The {RegistryExcelMeta.HEADERS.value[0]}s you enter are permanent and cannot be changed later.
    Only the other two values can be updated in future runs.

    Press **Enter** to continue..."""
    )

    REGISTRY_UPDATE_RECAP = dedent(
        """
                    RADIATORS REGISTRY REVIEW

    Radiators registry file found at: {registry_path}.

    Here are your current registered radiators:

    {registry_table}

    If you need to change a radiator's ID or coefficient, you can do so in the next step.

    Would you like to update any radiator's ID or coefficient? (yes/no)
    """
    )

    REGISTRY_UPDATE_DESCRIPTION = dedent(
        f"""
                    RADIATORS REGISTRY UPDATE

    You decided to update the data in the {Files.RADIATORS_REGISTRY} file.

    For each registered radiator, you'll be shown its ID, and coefficient.

    Please confirm the information is correct, or choose to modify it as needed.

    Press **Enter** to continue..."""
    )

    USAGE_GENERATION = dedent(
        f"""
                    USAGE FILE CREATION

    We're going to create the usage file: {Files.DEFAULT_USAGE_NAME}.
    This file will be saved in the {Folders.USAGE_FOLDER} folder and
    will be used to track radiator heat readings.

    Here's how it works:

    1. You'll enter the years to include in the file name.
       If you choose different years in future runs, a new file will be created,
       allowing you to keep data for each heating season separate.

    2. You'll choose the date format for recording when readings are taken:
       - {DateFormats.EU_LABEL} ({SharedConstants.EUROPEAN} format)
       - {DateFormats.US_LABEL} ({SharedConstants.AMERICAN} format)

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

    Press **Enter** to continue..."""
    )

    YEARS_FILENAME_ENTRY = dedent(
        """
                    ENTER YEARS

    Default filename for the usage file: {usage_file}

    Enter the two years for the heating season to include in the file name.
    They must be separated by a dash (YYYY-YYYY).
    For example, for the season starting in {start_year}, enter: {start_year}-{end_year}
    """
    )

    PROMPT_DATE_FORMAT = dedent(
        f"""
                    CHOOSE DATE FORMAT

    Type:

    - '{SharedConstants.EUROPEAN}' for {DateFormats.EU_LABEL}
    or
    - '{SharedConstants.AMERICAN}' for {DateFormats.US_LABEL}
    """
    )

    PROMPT_DATE_INPUT_MODE = dedent(
        f"""
                    DATE INPUT MODE

    Should dates be entered automatically or manually?
    Type '{SharedConstants.DATE_AUTO}' or '{SharedConstants.DATE_MANUAL}'
    """
    )

    USAGE_DATA_ENTRY_INTRO = dedent(
        """
                    USAGE FILE DATA ENTRY

    The usage file has been pre-filled with radiator data from your registry file.

    Next, depending on your configuration, dates may be added automatically or entered manually.
    You will then be asked to enter the valve setting for each radiator,
    followed by the corresponding raw reading from the HCA device.
    Lastly, you will have the option to add any notes about the day's readings.

    After you provide this information, the program will calculate the heat usage for each radiator.

    Press **Enter** to continue..."""
    )

    ENTER_MANUAL_DATE = dedent(
        """
                    ENTER DATE

    You chose to enter dates manually.
    Please provide the date for when the radiator recordings were taken."""
    )

    VALVE_SETTING_ENTRY = dedent(
        """
                    ENTER VALVE SETTING

    Please enter the valve setting for each radiator.
    You can enter numbers (e.g. 2), words (e.g. 'two'), fractions (e.g. '2 and a half'),
    decimals (e.g. '2.1'), or any description that matches your valve.
    If your valve is set to antifreeze, enter 'antifreeze'.

    Press **Enter** to continue...
    """
    )

    VALVE_SETTING_UPDATE = dedent(
        """
                    VALVE SETTING UPDATE

    Since the valve settings were already entered in a previous run, we'll now review them.
    For each radiator, you'll see the current valve setting and be asked if you want to modify it.
    If you wish to make a change, answer 'yes' when asked; else, the existing value will be kept.

    Remember, you can enter numbers (e.g. 2), words (e.g. 'two'), fractions (e.g. '2 and a half'),
    decimals (e.g. '2.1'), or any description that matches your valve.
    If your valve is set to antifreeze, enter 'antifreeze'.

    Press **Enter** to continue..."""
    )

    PROMPT_VALVE_UPDATE = dedent(
        """
    Current valve setting for '{radiator_name}': {current_valve_setting}
    Do you want to change it? (yes/no):
    """
    )

    ENTER_RAW_READINGS = dedent(
        """
                    RAW READINGS

    Please, enter the Raw Reading from the HCA device for each radiator.
    """
    )

    CHANGE_USAGE_CONFIG = dedent(
        """
                    MODIFY USAGE CONFIGURATIONS

    The usage file: {file_name} was created in a previous run. Below are the current configurations:

    - File Name: {file_name} (e.g., change the years to create a new file for a new heating season).
    - Date Format: {date_format} (e.g., European or American format).
    - Date Input Mode: {date_input} (e.g., manual or automatic).

    Having reviewed these configurations, do you want to modify any of them? (yes/no)
    """
    )

    OPEN_USAGE = dedent(
        """
    The usage file containing all radiator data is ready.
    Would you like to open it now? (yes/no)
    """
    )


# endregion.
