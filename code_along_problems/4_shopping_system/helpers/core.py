"""
Core functionality
"""
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Built In
import json
from pathlib import Path

# Union: A way to type hint that an object can be one of many types.
from typing import Union

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 3rd Party

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Owned




# =================================================================================================
# NOTE: I would remember the following syntax. Instead of relying paths relative to where the code,
# is run, we can use the path to THIS file as a reference for other paths we want to use.
# =================================================================================================

# Path to this core.py file.
# Ex: {wherever you put python101 files}/code_along_problems/4_shopping_system/helpers/core.py
THIS_FILES_PATH = Path(__file__).absolute()

# Given the path to this file, note the syntax below.

# The first .parent turns the path (THIS_FILES_PATH) into:
#   {wherever you put python101 files}/code_along_problems/4_shopping_system/helpers
# The second .parent turns the path into:
#   {wherever you put python101 files}/code_along_problems/4_shopping_system
# Then the `/` dives into the directory so the final path is:
#   {wherever you put python101 files}/code_along_problems/4_shopping_system/data/store_info.json
STORE_INFO_FILE_PATH = THIS_FILES_PATH.parent.parent / 'data' / 'store_info.json'

# Path to the audit logs file, similar to above.
LOGS_FILE_PATH = THIS_FILES_PATH.parent.parent / 'data' / 'logs.txt'

def read_store_info() -> Union[dict, None]: # The arrow is a type hint on the return value.
    """
    Read store_info from file store.
    """
    try:
        with open(STORE_INFO_FILE_PATH) as file_obj:
            return json.load(file_obj)
    except FileNotFoundError:
        print("The store_info file could not be found.")
        return None

def save_store_info(store_info: dict) -> None:
    """
    Save the store_info to file store.
    """
    # =============================================================================================
    # TODO This file was opened in read only but we are writing to it. Change the mode
    # to a mode that allows writing, truncates the file on write, and will create the file if
    # it does not exist. (1 line edit) [slide 43]
    # =============================================================================================
    with open(STORE_INFO_FILE_PATH) as file_obj:
        json.dump(store_info, file_obj, indent=4)
