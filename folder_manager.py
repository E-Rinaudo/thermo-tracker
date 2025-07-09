#!/usr/bin/env python3


# region Module Description And Imports.
"""Manages the creation of the Excel files folder."""

from __future__ import annotations

import logging
import os
import shutil
from pathlib import Path
from typing import Any

import pyinputplus as pyip  # type: ignore # pylint: disable=import-error

import constants as cons
import utils
from config_manager import ConfigManager

# Aliases for all the Enums of constants.py.
CKeys = cons.ConfigKeys
Files = cons.Files
Folds = cons.Folders
SCons = cons.SharedConstants
UserMsgs = cons.UserMessages


# endregion.


# region Manage Excel Folder.


class ExcelFolderManager:
    """Main class to manage the creation of the Excel folder for storing files.

    Handles the initialization, folder creation, and user interaction for
    setting up the folder where Excel files will be saved.

    Attributes:
        config_data (dict[str, str]): Data loaded from or to be saved in the
            JSON config file.
        generator (FolderGenerator): Instance of the FolderGenerator class.
        folder_path (str): The folder path where Excel files will be saved.
    """

    config_data: dict[str, Any]
    generator: FolderGenerator
    folder_path: str

    def __init__(self, config_data, config_update):
        """Initializes attributes and creates a FolderGenerator instance."""
        self.config_data = config_data
        self.generator = FolderGenerator(self.config_data, config_update)
        self.folder_path = SCons.EMPTY_STR  # Lazy initialization.

    def update_folder_path(self) -> None:
        """Updates the folder path based on the current configuration data.

        Retrieves the folder path from the configuration data and
        assigns it to the folder_path attribute.
        """
        self.folder_path = self.config_data[CKeys.EXCEL_FOLDER]

    def handle_folder_selection(self) -> None:
        """Handles the folder selection process.

        On the first run, prompts the user to choose between the default
        or a custom folder. On subsequent runs, asks if the user wants
        to create a new folder (e.g., after moving or changing
        radiators). If not, continues using the existing folder.
        """
        if pyip.inputYesNo(self._get_folder_prompt()) == SCons.AGREE:
            self._create_custom_folder(self.folder_path)
        else:
            self._create_default_folder()

    def _get_folder_prompt(self) -> str:
        """Checks if the Excel folder exists to select a message accordingly.

        Returns:
            The appropriate folder selection prompt for the user.
        """
        if not os.path.exists(self.folder_path):
            return UserMsgs.FOLDER_GENERATION.format(folder_path=self.folder_path)

        return UserMsgs.FOLDER_RESET_PROMPT.format(folder_path=self.folder_path)

    def _create_custom_folder(self, folder_path: str) -> None:
        """Handles the creation of a custom folder and files migration.

        Args:
            folder_path: The path to the Excel folder file.
        """
        self.generator.handle_custom_folder(folder_path)

    def _create_default_folder(self) -> None:
        """Creates the default folder only if it doesn't already exist."""
        if not os.path.exists(self.folder_path):
            self.generator.handle_default_folder()


# endregion.


# region Generate Excel Folder.


class FolderGenerator:
    """Handles the creation of the folder for Excel files.

    This class provides methods for creating custom folders, validating paths,
    and migrating files between folders.

    Attributes:
        config_data (dict[str, str]): Data loaded from or to be saved in the
            JSON config file.
        config_update (dict[str, bool]): Indicates if the configuration data
            needs to be updated.
        config (ConfigManager): Instance of the ConfigManager class.
    """

    config_data: dict[str, Any]
    config_update: dict[str, bool]
    config: ConfigManager

    def __init__(self, config_data, config_update) -> None:
        """Initializes attributes."""
        self.config_data = config_data
        self.config_update = config_update
        self.config = ConfigManager(self.config_data, self.config_update)

    def handle_custom_folder(self, folder_path: str) -> None:
        """Runs the process of creating a custom folder.

        Args:
            folder_path: The path to the Excel folder file.
        """
        while True:
            if self._generate_custom_folder(folder_path):
                self.config_update[SCons.UPDATE] = True
                break

    def _generate_custom_folder(self, folder_path: str) -> bool:
        """Generates a custom folder based on user input.

        Args:
            folder_path: The path to the Excel folder file.

        Returns:
            True if the folder was successfully created; False otherwise.
        """
        logging.info("User decided to use a custom folder for Excel files.")
        self._prompt_folder_path()

        if not self._validate_folder_path():
            return False

        if not self._assert_correct_location():
            return False

        # If the folder already exists, this means the user is starting over
        # (e.g., moved or changed radiators).
        if os.path.exists(folder_path):
            self._ensure_unique_folder_name(folder_path)
            self._handle_file_migration(folder_path)
            self.config.delete_config()

        self._make_folder()
        return True

    def _prompt_folder_path(self) -> None:
        """Asks the user to enter a custom path for the Excel files folder."""
        self.config_data[CKeys.EXCEL_FOLDER] = pyip.inputStr(UserMsgs.EXCEL_FOLDER_PROMPT)
        logging.info("Folder decided by the user: %s", self.config_data[CKeys.EXCEL_FOLDER])

    def _validate_folder_path(self) -> bool:
        """Validates whether the provided folder path exists.

        Returns:
            True if the folder is confirmed; False otherwise.
        """
        excel_folder = self.config_data[CKeys.EXCEL_FOLDER]

        if os.path.exists(os.path.dirname(excel_folder)):
            print(f"\nNew folder path: {excel_folder}")
            return True

        return self._invalid_path()

    def _invalid_path(self) -> bool:
        """Displays a warning if the entered path is invalid.

        Returns:
            False since the path is not a valid one.
        """
        print("\n❌ WARNING: The Path provided does not exist. Please enter a correct one.")
        logging.info("User chose a wrong path: %s.", self.config_data[CKeys.EXCEL_FOLDER])
        return False

    def _assert_correct_location(self) -> bool:
        """Asks the user to confirm the selected folder path.

        Returns:
            True if the user confirms the location; False otherwise.
        """
        confirm_location = f"Confirm: {self.config_data[CKeys.EXCEL_FOLDER]}? (yes/no)\n"
        if pyip.inputYesNo(confirm_location) == SCons.AGREE:
            return True

        print("\nOkay, provide a new path.")
        return False

    def _ensure_unique_folder_name(self, old_path: str) -> None:
        """Ensures the new folder name is unique if the user is starting over.

        If the new folder path matches the old one, appends a suffix to create
        a unique name.

        Args:
            old_path: Path to the Excel folder used in previous runs.
        """
        new_path = self.config_data[CKeys.EXCEL_FOLDER]
        if old_path == new_path:
            utils.display_user_info(
                UserMsgs.SAME_FOLDER_NAME.format(
                    new_folder=os.path.basename(new_path), old_folder=os.path.basename(old_path)
                )
            )
            self.config_data[CKeys.EXCEL_FOLDER] = new_path + Folds.FOLDER_NAME_SUFFIX
            logging.info("Appended suffix to: %s", self.config_data[CKeys.EXCEL_FOLDER])

    def _handle_file_migration(self, old_path: str) -> None:
        """Handles file migration if the folder path has changed.

        Checks if migration is needed and, if so, displays the contents
        of the old folder and migrates files to the new folder.

        Args:
            old_path: Path to the Excel folder used in previous runs.
        """
        new_path = self.config_data[CKeys.EXCEL_FOLDER]
        self._recap_folder_content(old_path)
        self._copy_old_files(old_path, new_path)

    def _recap_folder_content(self, old_path: str) -> None:
        """Displays a message and lists the contents of the old folder.

        Args:
            old_path: The path of the old folder to display.
        """
        utils.display_user_info(UserMsgs.OLD_FILES_INFO)

        for file in Path(old_path).rglob(Files.XLSX):
            print(f"- {file}")

    def _copy_old_files(self, old_path: str, new_path: str) -> None:
        """Prompts whether to migrate files from the old folder to the new one.

        Args:
            old_path: Source folder.
            new_path: Destination folder.
        """
        copy_prompt = UserMsgs.COPY_OLD_FILES.format(old_path=old_path, new_path=new_path)

        if pyip.inputYesNo(copy_prompt) == SCons.AGREE:
            logging.info("User decided to move files from %s to %s", old_path, new_path)
            shutil.copytree(
                old_path, os.path.join(new_path, os.path.basename(old_path)), dirs_exist_ok=True
            )
            print("\n✅ Files copied successfully to the new folder.")
        else:
            print("Files remain in the previous folder. You can move them manually if needed.")

    def handle_default_folder(self) -> None:
        """Creates the default folder if it doesn't already exist."""
        logging.info("User decided to use default folder for Excel files.")
        self._make_folder()
        self.config_update[SCons.UPDATE] = True

    def _make_folder(self) -> None:
        """Creates a folder for the Excel files."""
        folder = self.config_data[CKeys.EXCEL_FOLDER]
        logging.info("Creating %s as folder", folder)
        os.makedirs(folder, exist_ok=True)
        print(f"\n✅ Folder ready: {folder}\nAll Excel files will be saved here.\n")


# endregion.
