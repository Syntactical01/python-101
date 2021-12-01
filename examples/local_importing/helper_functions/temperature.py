"""
Simple functions to work with temperatures.
"""

# Owned
from constants import TEMP_DELTA

def fahr_to_cels(fahr: float) -> float:
    """
    Convert a given temp in fahrenheit to celsius.
    """
    cels = (5 / 9) * (fahr - TEMP_DELTA)
    return cels

def cels_to_fahr(cels: float) -> float:
    """
    Convert a given temp in celsius to fahrenheit
    """
    fahr = (9 / 5) * cels + TEMP_DELTA
    return fahr
