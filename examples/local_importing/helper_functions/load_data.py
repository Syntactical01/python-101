"""
Load the text from the csv file in the data folder.
"""
# Builtin
from pathlib import Path

# Useful copy and pasteable code.

# .../local_importing/helper_functions
_PATH_TO_PARENT_DIR = Path(__file__).parent.absolute()

# .../local_importing/data/example_data.csv
PATH_TO_DATA = _PATH_TO_PARENT_DIR.parent / 'data' / 'example_data.csv' 

def get_example_data():
    """
    Return the text from the example_data.csv file.
    """
    with open(PATH_TO_DATA) as file_obj:
        return file_obj.read()

