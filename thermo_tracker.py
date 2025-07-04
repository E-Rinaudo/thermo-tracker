#!/usr/bin/env python3


# region Module Description And Imports.
"""THERMO TRACKER - Radiator Heat Usage Tracking (CLI Application)
================================================================================

This program records heat usage data from radiators equipped with ISTA heat cost
allocators (HCAs), devices that measure heat release to calculate heating
consumption. ISTA, a German brand, is known for its high-quality HCAs used in
residential and commercial buildings.

Developed for personal use, this tool helps track actual heat consumption instead
of relying solely on raw readings. It automates data collection, calculations,
and storage in Excel files for easy review.

Program Workflow:
-----------------
1. During the initial setup, the user selects a folder to store the program's data.
   The program creates this folder and generates essential files, including a
   registry file (*radiators_registry.xlsx*). This registry contains static
   radiator data (Radiator Name, Radiator ID, and ISTA coefficients) provided
   by the user.
2. On subsequent runs, the program loads and verifies the static data with the user.
3. The user then enters the raw readings from the HCAs for each radiator,
   along with the valve setting and any notes they wish to add.
4. The program calculates actual heat usage by multiplying the raw reading
   by its corresponding coefficient.
5. All data along with dates are stored in a structured Excel file
   (**radiators_usage_[Years].xlsx**) for easy review.
6. The user is notified when the data is saved and can choose to open the file.
"""

import logging
from typing import Any, cast

import constants as cons
import logging_file
import utils
from config_manager import ConfigManager
from folder_manager import ExcelFolderManager
from registry_manager import RegistryManager
from usage_manager import UsageManager

# Aliases for all the Enums of constants.py.
TInst = cons.ThermoInstances
UserMsgs = cons.UserMessages
SCons = cons.SharedConstants

# List of manager classes used to initialize instances in ThermoTracker.
_MANAGERS = (ConfigManager, ExcelFolderManager, RegistryManager, UsageManager)

# Set up the logging configuration.
logging_file.logging_configuration()
logging_file.disable_logging()


# endregion.


# region Main Controller Class For The Application.


class ThermoTracker:
    """Main controller class for the Thermo Tracker application.

    Attributes:
        config_data (dict[str, str]): Stores configuration data.
        config_update (dict[str, bool]): If the configuration data need an
            update.
        instances (dict[TInst, object]): Holds instances of manager classes.
    """

    config_data: dict[str, Any]
    config_update: dict[str, bool]
    instances: dict[TInst, object]

    def __init__(self) -> None:
        """Initializes attributes and manager modules instances."""
        self.config_data = {}
        self.config_update = {SCons.UPDATE.value: False}
        self.instances = {
            t_inst_key: manager(self.config_data, self.config_update)
            for t_inst_key, manager in zip(TInst, _MANAGERS)
        }

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

    def _get_config_manager(self) -> ConfigManager:
        """Gets the ConfigManager instance with casting for type safety.

        Returns:
            The ConfigManager instance.
        """
        return cast(ConfigManager, self.instances[TInst.CONFIG])

    def _get_folder_manager(self) -> ExcelFolderManager:
        """Gets the ExcelFolderManager instance with casting for type safety.

        Returns:
            The ExcelFolderManager instance.
        """
        return cast(ExcelFolderManager, self.instances[TInst.FOLDER])

    def _get_registry_manager(self) -> RegistryManager:
        """Gets the RegistryManager instance with casting for type safety.

        Returns:
            The RegistryManager instance.
        """
        return cast(RegistryManager, self.instances[TInst.REGISTRY])

    def _get_usage_manager(self) -> UsageManager:
        """Gets the UsageManager instance with casting for type safety.

        Returns:
            The UsageManager instance.
        """
        return cast(UsageManager, self.instances[TInst.USAGE])

    def save_app(self) -> None:
        """Saves the current configuration to the JSON file."""
        self._get_config_manager().save_config()
        logging.debug("Closing the program.")


# endregion.


if __name__ == "__main__":
    thermo_tracker = ThermoTracker()
    thermo_tracker.run_app()
    thermo_tracker.save_app()
