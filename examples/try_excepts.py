"""
Code used by the PowerPoint to show how to use try/excepts.
"""

# Comment out the try except code to see what happens without the
# try/except.
try:
    year = input("Year of birth: ")
    result = 2020 - year
    print(f"Result {result}")
    raise RuntimeError # This will trigger the last except clause.
except TypeError as e:
    print(f"Could not figure out date of birth ({year=}). Error - {e}")
except KeyError: # Exceptions can be chained
    print("A key error occued")
except Exception: # And we can also generically catch all exception.
    print("Clause entered")
    raise

