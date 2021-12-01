"""
# =================================================================================================
# 
#  Purpose: This program computes the tax amount a person has to pay
#           given the base salary and wether they pay in-state 
#           or out-of-state tax.
#
#  Reference slides from the presentation:
#       - Variable Naming/Assigment 7
#       - Input/output example:     8
#       - Primitive Types:          10
#       - f-strings:                11
#       - Truthy/Falsey Values:     12
#       - Branching:                13
#
#  Inputs : State of residence (string) of the user stored as the variable `state`
#          Base salary of the user (float) stored as `base_salary`. 
# 
#  Outputs : Tax amount the person has to pay.
# 
# =================================================================================================
"""

IN_STATE_RATE = 0.075
OUT_STATE_RATE = 0.15

# For best practice purposes we are going to create
# a function called main where we will put all the code that will be ran.
# We will cover functions later in the hack so don't worry about it,
# just make sure all code you write within the function is properly
# indented.
def main():
    # =============================================================================================
    # TODO 1: Before making any edits, run the program.
    # 1) First, the program will error with "IndentationError" for `tax_rate` below. Indentations
    #    for python are important. The norm is to indent with 4 spaces per indent but technically you
    #    can indent however you want BUT you must be **CONSISTENT**. Fix `tax_rate` by dedenting
    #    one space and running the program again.
    #
    # 2) Second, the program will error with "TabError" on `tax_due`.
    #    Python can use tabs (\t) or spaces for indention. The norm is to use spaces and
    #    Visual Studio Code defaults to using spaces when you hit the [Tab] key; however, if you
    #    were to open this code in notepad for example, the [Tab] key would use a
    #    tab character(\t) instead of spaces. Python can handle indenting via tabs OR spaces,
    #    but not both. Before `tax_due` I put a tab instead of four spaces. An easy way to find
    #    tabs is to highlight the line where the error occured one character at a time until you
    #    notice something big be highlighted (basically it will appear to highlight four spaces
    #    at one). Remove the tab and replace it with 4 spaces and the program should run without
    #    error.
    # =============================================================================================

    # These variables do not need to be declared before hand like this
    # but it will probably be useful to see some of the variables you
    # should be using up front which is why I did it.

    state = None       # variable to store state of residence (string)
    base_salary = None # varaiable to store the base salary (float)
    tax_rate = None    # variable to store tax rate based on state of residence (float)
    tax_due = None     # variable to store the dollar amount to pay in taxes (float)

    # =============================================================================================
    # TODO 2: Add an input() statement for the user to enter their `state`. (1 line) [slide 8]
    # =============================================================================================
    state = input("Enter your state of residence (AA-ZZ): ")




    # =============================================================================================
    # TODO 3: Add an input() statement for the user to input their `base_salary`.
    # (1 line) [slide 8]
    # =============================================================================================
    base_salary = input("Enter your salary: ")




    # =============================================================================================
    # TODO 4: Convert the salary input (TODO 3) to a float. (1 line) [slide 10]
    #
    # Hint: We can convert a string to an integer via: my_int = int(my_input)
    #   What would the similar opertion be for converting to a float?
    #
    # Also note, the right hand side of the assignment (=) is done fully before the left.
    # This means that the following is valid: `my_input = int(my_input)`. The old `my_input`
    # would be converted to an integer, then reassigned to a new `my_input`.
    # =============================================================================================
    base_salary = float(base_salary)




    # =============================================================================================
    # TODO 5: Check if the inputted state (TODO 2) is WI, MN, or IL and set the
    # `tax_rate` (defined right inside the main function) to `IN_STATE_RATE` (defined under the
    # file docstring at the top), else set the `tax_rate` to `OUT_STATE_RATE`.
    # 
    # (1 to ~6 lines) [slide 7 & 13]
    #
    # Hint: Some syntax that *may* be useful (if, elif, else, ==, !=, or)
    # =============================================================================================
    if state == 'MN' or state == 'WI' or state == 'IL':
        tax_rate = IN_STATE_RATE
    else:
        tax_rate = OUT_STATE_RATE
    # Another option after learning list:
    # tax_rate = IN_STATE_RATE if state in ['MN', 'WI', 'IL'] else OUT_STATE_RATE




    # =============================================================================================
    # TODO 6: Calculate the `tax_due` for the given `base_salary` and `tax_rate` and
    # assign it to a variable. [slide 7]
    #
    # The amount do (`tax_due`) should be the inputted salary multiplied by the tax rate.
    # =============================================================================================
    tax_due = base_salary * tax_rate




    # =============================================================================================
    # TODO 7: Print the `tax_due` to the user in a friendly message using f-strings. [slide 11]
    #
    # Hint: Format strings look like this: `f""` (note the leading `f`)
    #
    # OPTIONAL: Can you output the `tax_due` `round`ed to 2 decimal places?
    # (Requires a google search)
    # =============================================================================================
    print(f"Uncle Sam's share is ${tax_due}.")
    # print(f"Uncle Sam's share is ${round(tax_due, 2):.2f}.")




# =================================================================================================
# EXTRAS: Please make sure the program runs before attempting any of the follow extra activities.
#
#   1) The above program has some "Edge Cases" that we do not account for, can you try fixing the
#      program so the following edge cases don't cause unexpected behavior? [slide 10, 13]
#           - A non-number salary is entered - Example: "foobar"
#           - A negative salary is entered.
#
#   2) Can you add a input called `dependents`, which should just be a yes or no answer (boolean)
#      and if the user has dependents, then halve their tax_rate before calculating the tax_due.
#      [slide 7, 8, 10, 13]
#       
# =================================================================================================


# When python runs this file with something like:
#   `python entrypoint.py`
# it will assign '__main__' to the __name__ variable.
# Thus we can call our main code like this.
if __name__ == '__main__':
    main()

# In theory we could do all this code without the two lines above
# and without the `def main()` up top but we will go over later
# why we do it this way (it's just a best practice).
