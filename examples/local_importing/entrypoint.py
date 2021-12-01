"""
Entry point to the program that helps demonstrate import
between local files.
"""
# Owned
import constants
from constants import PI
from helper_functions import BOOT
from helper_functions.temperature import fahr_to_cels
from helper_functions.hackathon import trade_secret
from helper_functions.load_data import get_example_data

def main():
    """
    Main entry point to the program
    """
    print("Program Started")
    print(f"{PI=} {constants.MOL=}")

    print(f"{BOOT=}")

    temp_f = 98
    print(f"The temperature is {temp_f}F or {fahr_to_cels(temp_f)}")

    print(f"Super secret info - {trade_secret.MY_SECRET_DATA}")
    
    print(f"CSV Data: \n{get_example_data()}")
    
if __name__ == '__main__':
    main()
