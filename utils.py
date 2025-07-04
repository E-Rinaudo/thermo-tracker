#!/usr/bin/env python3


# region Module Description.
"""Utility methods shared across the Thermo Tracker application."""


import os
from typing import Any

import constants as cons

# Aliases for all the Enums of constants.py.
CKeys = cons.ConfigKeys
SCons = cons.SharedConstants
Files = cons.Files
Folds = cons.Folders


# endregion.


# region Methods Shared Among Modules.


def display_user_info(msg: str, value: str = SCons.EMPTY_STR.value) -> None:
    """Displays a message to the user and waits for them to press Enter.

    It is used for informational screens that require acknowledgment
    before continuing, such as the program introduction or the creation
    process for Excel files.

    Args:
        msg: The message to display.
        value: The optional value to format into the message.
    """
    input(msg.format(value=value))


def update_config_path(
    config_data: dict[str, Any],
    config_update: dict[str, bool],
    path_key: CKeys,
    path_suffix: Files | Folds,
) -> None:
    """Updates the path for a given key in the configuration dictionary.

    Then, checks if the path for the specified key has changed.
    If it has, the configuration update flag is set to True.

    Args:
        config_data: The configuration dictionary to update.
        config_update: Indicates if the configuration data needs to be updated.
        path_key: The key in the configuration dictionary to update.
        path_suffix: The file or folder name to append to the base path.
    """
    # Used to detect folder changes.
    old_path = config_data.get(path_key.value)

    config_data[path_key.value] = os.path.join(
        config_data[CKeys.EXCEL_FOLDER.value], path_suffix.value
    )

    # If the path has changed, mark the configuration as needing an update.
    if old_path != config_data[path_key.value]:
        config_update[SCons.UPDATE.value] = True


def get_radiators_owned(config_data: dict[str, Any]) -> int:
    """Gets the radiators owned from the config_data dictionary.

    Args:
        config_data: The configuration dictionary.

    Returns:
        The number of radiators owned.
    """
    return config_data[CKeys.RADIATORS_OWNED.value]


# endregion.
