#!/usr/bin/env python3


# region Module Description And Imports.
"""Manages the JSON configuration file for the Thermo Tracker application.

This module provides functionality to load, save, and update the JSON
configuration file, which stores user preferences and application
settings.
"""

import json
import logging
import os
from typing import Any

import constants as cons

# Aliases for all the Enums of constants.py.
CKeys = cons.ConfigKeys
Files = cons.Files
Folds = cons.Folders
SCons = cons.SharedConstants


# endregion.


# region JSON Config File Manager.


class ConfigManager:
    """Manages the opening, saving and update of the JSON config file.

    The JSON file stores user preferences and application settings, such as
    folder paths, file names, and other configuration options.

    Attributes:
        config_data (dict[str, str]): Data loaded from or to be saved in the
            JSON config file.
        config_update (dict[str, bool]): Indicates if the configuration data
            needs to be updated.
    """

    config_data: dict[str, Any]
    config_update: dict[str, bool]

    def __init__(self, config_data, config_update) -> None:
        """Initializes attributes."""
        self.config_data = config_data
        self.config_update = config_update

    def open_config(self) -> None:
        """Loads saved settings from the config file, if available.

        If the config file does not exist (first run), fall back to
        default values and initialize the configuration accordingly.
        """
        try:
            with open(Files.CONFIG_FILE, "r", encoding="utf-8") as file:
                logging.info("Retrieving info from the config file.")
                config = json.load(file)
        except FileNotFoundError:
            logging.info("The config file has not been generated yet.")
            # Only the DEFAULT_EXCEL_FOLDER is set here, as other settings are
            # not needed at this stage and can be configured by the user later.
            self.config_data[CKeys.EXCEL_FOLDER] = Folds.DEFAULT_EXCEL_FOLDER
        else:
            self.config_data.update(config)

    def save_config(self) -> None:
        """Saves the settings to a JSON configuration file for future use."""
        if self.config_update[SCons.UPDATE]:
            os.makedirs(Folds.CONFIG_FOLDER, exist_ok=True)

            with open(Files.CONFIG_FILE, "w", encoding="utf-8") as config:
                logging.info("Writing to the config file.")
                json.dump(self.config_data, config, indent=4)

    def delete_config(self) -> None:
        """Deletes the JSON configuration file to ensure a clean setup."""
        if os.path.exists(Files.CONFIG_FILE):
            os.remove(Files.CONFIG_FILE)
            logging.info("Config file deleted.")


# endregion.
