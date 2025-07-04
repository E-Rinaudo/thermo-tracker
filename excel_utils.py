#!/usr/bin/env python3


# region Module Description.
"""Shared utility methods for handling Excel files in Thermo Tracker.

The primary purpose of this module is to define reusable methods for
operations using the OpenPyXL library.
"""

import logging
from typing import Type

import openpyxl  # type: ignore # pylint: disable=import-error

import constants as cons

# Aliases for all the Enums of constants.py.
RegMeta = cons.RegistryExcelMeta
UsgMeta = cons.UsageExcelMeta
SNums = cons.SharedNumbers


# endregion.


# region Methods Shared Among Excel Modules.


class ExcelSharedMethods:
    """A utility class for methods shared across Excel-related modules.

    It provides reusable methods for customizing and saving Excel workbooks.
    These are used by modules that handle Excel files, such as the registry and
    usage managers.

    Attributes:
        workbook (Workbook): The Excel workbook object.
        worksheet (Worksheet): The active worksheet within the workbook.
    """

    workbook: openpyxl.Workbook
    worksheet: openpyxl.worksheet.worksheet.Worksheet

    def __init__(self, workbook, worksheet) -> None:
        """Initializes attributes."""
        self.workbook = workbook
        self.worksheet = worksheet

    def customize_worksheet(self, label: str, meta: Type[RegMeta | UsgMeta]) -> None:
        """Customizes the worksheet layout.

        Sets the title, freezes header rows, and adjusts column widths based
        on the provided metadata.

        Args:
            label: Descriptive label for logging (e.g. "registry", "usage").
            meta: Enum containing sheet metadata (e.g., headers, column widths)
        """
        logging.info("Customizing the %s worksheet.", label)
        self.worksheet.title = meta.SHEET_NAME.value
        self.worksheet.freeze_panes = meta.FREEZE_HEADERS.value

        for col, header in zip(meta.COLS.value, meta.HEADERS.value):
            self.worksheet.column_dimensions[col].width = len(header) + meta.COL_EXTRA_SPACE.value

            # Only UsageExcelMeta has NOTES_COLUMN_SPACE and the notes column is always "I".
            if hasattr(meta, "NOTES_COLUMN_SPACE") and col == meta.COLS.value[SNums.EIGHT.value]:
                self.worksheet.column_dimensions[col].width = meta.NOTES_COLUMN_SPACE.value

    def save_workbook(self, file_path: str, label: str) -> None:
        """Saves the workbook to the specified path and shows related messages.

        Args:
            file_path: Path to save the workbook.
            label: Short identifier of the file type (e.g. "registry", "usage").
        """
        self.workbook.save(file_path)
        message = f"✅ {label.capitalize()} file saved successfully to {file_path}."
        logging.info(message)
        print(message)


# endregion.
