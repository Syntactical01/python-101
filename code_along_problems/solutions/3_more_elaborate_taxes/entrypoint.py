"""
# =================================================================================================
# 
#  Purpose: This program computes the federal tax paid by several different
#           people based on their income and corresponding tax bracket.
#           For convenience we will just assume that people pay a certain percentage
#           based on their salary and we will NOT implement the bracket tax system
#           the USA uses. (You can do this in the future for extra practice).
#
#  Reference slides from the presentation:
#       - ** All slides used by the last problem: `2_simple_taxes` **
#       - Exceptions:       16
#       - Lists:            25
#       - For Loops:        26-29
#       - Dictionaries:     33-35

#
#  Input : State of residence of the user stored as the variable `state`
#          Base salary of the user stored as `base_salary`. 
# 
#  Output : Tax amount the person has to pay.
# 
# =================================================================================================
"""

# We can use json to print dictionaries and lists cleaner
# by using:
#
#   print(json.dumps(my_dict_or_list, indent=2))
#
# Imports should almost always be at the top of your file. (under the header comments)
# Import statements and json will be gone over at a later time in the presentation,
# just not the syntax above and try it out later when specified in the TODO.
import json

TAX_BRACKETS = [
    # percent_to_pay, minimum_income_inclusive, maximum_income_exclusive
    [10, 0, 9700],
    [12, 9700, 39475],
    [22, 39475, 84200],
    [24, 84200, 160725],
    [32, 160725, 204100],
    [35, 204100, 510300],
    [37, 510300, float('inf')],
]

# =================================================================================================
# TODO 1: It seems I made a typo in the following code. Run
# the code to figure out what I missed. Pylint may give it to you by highlighting the line,
# but it is important to be able to read and understand errors. (1 line to fix) [slide 16]
# =================================================================================================
# NOTE: Sometimes the error is not exactly where the traceback message says it is,
# but instead, it is **right** before where the traceback says it is.
# =================================================================================================
# NOTE: After the fix is applied, you should get a SyntaxError for `&&&` from later on
# in the program. This means your fix worked.
# =================================================================================================
SOME_PEOPLE = [
    {
        'name': 'Bill Gates',
        'company': 'Microsoft',
        'salary': 544300,
    },
    {
        'name': 'Little Billy',
        # NOTE using double quotes so a single quote can be used in the string itself:
        'company': "Little Billy's Lemonade Stand",
        'salary': 501,
    },
]


def main():

    # =============================================================================================
    # NOTE: Replace ALL instances of `&&&` with proper syntax and add code where specified
    # to get the program to run properly.
    # =============================================================================================

    # =============================================================================================
    # TODO 2: Using a `for` loop, loop through each `person` in `SOME_PEOPLE`... (1 line)
    # =============================================================================================
    for person in SOME_PEOPLE:
        # =========================================================================================
        # TODO 2 (cont) ... and print each each dictionary (which represents a person) to terminal.
        # Reference line 29 above for using json to make the print cleaner (1 line) [slide 8].
        # If you changed the indent, to a smaller value, can you see what happens?
        # NOTE: After TODO 2 is done, try running the code. It should work without erroring.
        # =========================================================================================
        print("Person we are currently working with:\n", json.dumps(person, indent=2))




        # =========================================================================================
        # TODO 3: For convenience, assign the `salary` and the `name` of the person to variables
        # called `salary` & `name` respectively. (1-2 lines) [slide 33]
        # =========================================================================================
        salary = person["salary"]
        name = person["name"]




        # =========================================================================================
        # TODO 4: Uncomment all lines between the @s below. You can do this quickly by highlighting
        # ALL the lines between @s and doing `Ctrl + /`. If you do it manually, make
        # sure to remove the `#` and the extra space ( ) that goes with it.
        #
        # Now that we have the person, we need to figure out what tax bracket they are in.
        # For loop through `TAX_BRACKETS` using tuple unpacking to get the following variable
        # out of each list:
        #   percent_to_pay
        #   minimum_income_inclusive
        #   maximum_income_exclusive
        #   (1 line to fix)
        #   [slide 31, 34 can also be useful]
        # =========================================================================================
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        for percent_to_pay, minimum_income_inclusive, maximum_income_exclusive in TAX_BRACKETS:

            # ===================================================================================
            # TODO 5: Curse my laziness. I left a `pass` here to come back to it, but I never
            # finished this logic. Add in `if` statement to see if the persons `salary` is
            # between the minimum_income_inclusive and maximum_income_exclusive using something
            # like if a < n < b: (NOTE: Is < the right operator for this?) If the salary is
            # between the lower and upper bound, then `break` out of this innerloop.
            # (2 lines - and the `pass` should be removed)
            # [slide 14 & 28]
            # NOTE: AFter TODO 5 is done, the code should be runable.
            # ===================================================================================
            if minimum_income_inclusive <= salary <= maximum_income_exclusive:
                break
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



        # =========================================================================================
        # NOTE: Even though we broke out of our `for` loop, the variables still exist
        # in this context (you can this yourself if you add a `print(vars())` and
        # quick;y rerun your code) meaning we can still use the three variables you created with
        # the above `for` loop. Since we broke out of the loop right when we found which
        # tax bracket the person is in, that means the **first** variable of your for loop above
        # contains the tax percentage that person will pay.
        # =========================================================================================

        # =========================================================================================
        # TODO 6 - Calculate the federal tax the person will pay using the first variables
        # for your for loop above and the person's `salary`,
        # NOTE: The tax rate is a percentage represented as a whole number (Ex: 95 instead of .95)
        # so you may need to convert that number to a decimal. (1 or 2 lines)
        # `tax_due` should be caclucated by multiple the persons `salary` time their
        # `percent_to_pay`.
        # (1 line) [Reference the last programming problem]
        # =========================================================================================
        tax_rate = percent_to_pay / 100
        tax_due = salary * tax_rate




        # =========================================================================================
        # TODO 7 - Time to do the print. Add a print statement which outputs
        # a message similar to the following:
        #
        #   John Smith will pay 332.33 in taxes.
        #
        # NOTE: The number should be rounded to two decimals places. To figure out
        # how to do this google something like:
        #
        #   "python fstring round string to two decimal places"
        #
        # Stackoverflow will be your best friend for learning new things quickly. I recommend
        # jumping straight for the StackOverflow links over any form of blog post.
        #
        # (1 line) [slide 11]
        # =========================================================================================
        print(f"Uncle Sam's share for {name} is ${round(tax_due, 2):.2f}.") # `:.2f` pads the float to two decimal places




        # =========================================================================================
        # EXTRAS:
        # CONGRATS, the program is done and should run. Ask questions if you have them or you can
        # look into refactoring the code to address the following edge cases if you have time.
        #   1) Add some more people to SOME_PEOPLE to make sure your program works if we
        #      add more people.
        #   2) What would happen if someones enters a negative salary? Can you fix this?
        #     [slide 13 may be useful as well as 17]
        #   3) Lets say I listed `Bill Gates` twice with two different incomes. Could you combine
        #      all his incomes before calculating his taxes due? [slide 17 & 33 could be helpful]
        #   4) [Much Longer Extra] Could you change the code to find the taxes due using the
        #      actual progressive tax system? https://www.investopedia.com/terms/t/taxbracket.asp
        # =========================================================================================

if __name__ == '__main__':
    main()
