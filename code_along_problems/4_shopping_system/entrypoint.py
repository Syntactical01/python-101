"""
This is a simple shopping program.
Walk through the TODO(s) to finish the program.

The goal of the program is to buy products from a store (stored in a json file)
and return a billable amount for all products purchased. When the program
is done running, we need to make sure the `store_info.json` is properly updated
so that have an accurate inventory the next time the program is run.

This program will be the hardest with the least hand holding. I want to give
you something to work on and try to solve on your own. Good chance
this won't be finished during the break out session, but work through
it and ask questions if needed. Try to get as far as you can.

HINT: Need help solving a bug? Add `print` statements throughout the code
to see what the variables are. Or use a `breakpoint()` which is talked about
underneath TODO 4 below.
"""

# Built In
import json
from typing import Tuple

# 3rd Party

# Owned
from helpers.core import read_store_info

# =================================================================================================
# TODO 1: Import `save_store_info` from helpers.core (1 line)
# [Reference the folder examples/local_importing]
# =================================================================================================





def go_buy_products(shopping_list: dict) -> Tuple[dict, float]:
    """
    Returns the products purchased and a bill amount.
    ARGUMENTS:
        shopping_list (dict):
            A dictionary where the key is the product we want purchased and the value
            is the quantity we want - Example:
                {
                    "Peanut Butter": 1,
                    "Mushrooms": 0,
                    "Animal Crackers": 2,
                }
    RETURNS:
        Returns a tuple of two elements:
            1st) A dictionary where the product name maps to the quantity purchased
            2nd) A float containing the change left over.
            Example:
                (
                    {
                        "Peanut Butter": 1,
                        "Animal Crackers": 1,
                    },
                    4.23
                )
    """
    print(f"Buy products called with shopping list:\n{json.dumps(shopping_list, indent=4)}")
    items_purchased = dict()
    billable_amount = 0

    # =============================================================================================
    # TODO 2: Read the store info JSON file but calling the `read_store_info` function
    # imported above, and assign it to a variable. (1 line) [slide 39]
    # =============================================================================================




    # =============================================================================================
    # TODO 3: Specifically pull the `inventory` from the store info dictionary (TODO 2) into a new
    # variable. (1 line) [slide 33]
    # =============================================================================================




    # =============================================================================================
    # TODO 4: At this point the program should run. Add a print to print out the stores inventory
    # from TODO 3.  You can just print the dictionary itself, add a message and print the dict,
    # or iterate the dictionary and print each item in a more meaningful matter. Run the program
    # to make sure it prints what you expect. (1-4 lines) [slides 11 & 35 can be useful]
    # =============================================================================================




    # =============================================================================================
    # HINT: Want a useful syntax for debugging? On the line below this block, invoke the function
    # `breakpoint()` (when done playing with breakpoint remove it / comment it out).
    #
    #   - breakpoint() : When this function is called the code, python will enter a
    #                    Pdb (Python Debugger). Basically this allows you to type in valid python
    #                    code to see what you program is doing. Type in `vars()` to see the
    #                    currently defined variables. Add a couple `print`s on those variables
    #                    to experiment with the debugger. One you are done debugging, type
    #                    `continue`and python will exit the debugger and continue running the code.
    # =============================================================================================



    # =============================================================================================
    # TODO 5: Go to the `inventory_list_to_dict` function below....
    # =============================================================================================
    # =============================================================================================
    # TODO 7: Invoke the `inventory_list_to_dict` function and pass it the variable you created
    # in TODO 3. Assign the return value of the function to the same variable you created in
    # TODO 3. i.e. we are overwriting the list of inventory items with its dictionary version.
    # (1 line) [slide 39].
    # =============================================================================================




    # =============================================================================================
    # In order to purchase items we need to iterate over the `shopping_list` and for each product
    # the invoker wants to purchas, we need to:
    #   1) Make sure that product is in the stores inventory
    #   2) Reduce the stores inventory by the amount purchased
    #   3) Calcuate how much we will bill the invoker based on the amount purchased.
    #
    # TODO 8: [Read TODO 9 before starting to see what is coming next]
    # Create a `for` loop to iterate over the `shopping_list` dictionary.
    # You will need the `product_name` and `quantity_wanted` for each product, you can decide if
    # you want to iterate over the dictionary keys only (then use the key to get the value)
    # or unpack the key and value in one go using .items()
    # (1-3 lines for `for` loop and variable assignment) [slide 34]
    # =============================================================================================





        # =========================================================================================
        # Now that you iterate over the shopping list, we need to check the `product_name`
        # against the stores inventory (TODO 7) to see if the store has it. We will then buy
        # inventory up to the amount we want or as much as we can get. The comments below
        # will explain each step you need to implement to do this.
        #
        # TODO 9: Implement the psuedo code below by reading the comments and writing the code
        # you think should match.
        # If the comment is indented, then the code you write should be indented to that level.
        # =========================================================================================
        
        # [PSUEDO CODE 1 (PC 1)]: If the product name (TODO 8) is in inventroy (TODO 7)
        # (1 line) [slide 13]


            # [PSUEDO CODE 2]: Extract the `on_hand` amount and the `cost_per_unit` from the
            # product dictionary (from the inventory) for this product name (PC 1)
            # into two similarly named variables (1-2 lines) [slide 33]
            # Take a look at data/store_info.json to see what the dictionaries look like.
            # You will need to use two keys ([key_1][key_2]) first key to get the product from
            # this list of products in inventory using the product's name
            # and the second key to get the needed variables within the product (such as on_hand)


            # [PSUEDO CODE 3]: Figure out which is smaller the `quantity_wanted` (TODO 8) or
            # the `on_hand` (PC 2) from the product and store this `min` value in a new variable.
            # This is the amount of the product we will purchase.
            # (1-4 lines) [slide 13 OR 25]

            # [PSUEDO CODE 4] if the smallest value (PC 3) is not equal to 0 (1 line) [slide 13]
            
                # [PSUEDO CODE 5] Multiply the `cost_per_unit` (PC 2) times the amount we will
                # purchase (PC 3) and add this amount to the `billable_amount` variable.
                # (1-2 lines)

                # [PSUEDO CODE 6] Add the quantity purchased (PC 3) to the `items_purchased`
                # dictionary for this `product_name` (TODO 8). (1 line) [slide 33]

                # [PSUEDO CODE 7] Subtract the quantity purchased (PC 3) from the inventory
                # product's `on_hand` quantity. Code should be similar to PC 2.




    # =============================================================================================
    # TODO 10: Invoke the `inventory_dict_to_list` function and pass it the dictionary we have been
    # working with from TODO 7. Assign the return value to a new variable so that
    # we can use it later. (1 line)
    # =============================================================================================




    # =============================================================================================
    # TODO 11:
    # We read the store info back in TODO 2, now we need to overwrite its inventory with our new
    # inventory so we can save all store info in one go. When updating a JSON document we always
    # do a full rewrite of the file, we can't (easily) update a subset of lines.
    # (1 line) [Someting like `store_info['inventory'] = TODO_10`]
    # =============================================================================================




    # =============================================================================================
    # TODO 12: Call the `save_store_info` function and pass the variable from
    # TODO 2 (used in TODO 10). This will save the store info back to the JSON file.
    # TIP: I left a bug in the core.py file that this will raise. Go read the TODO there to fix it.
    # =============================================================================================




    return items_purchased, billable_amount
            
            


def inventory_list_to_dict(inventory: list) -> dict:
    """
    Convert the list of inventory items to a dictionary.
    ARGUMENTS:
        inventory (list): A list containing the stores inventory (dicts). Something like:
            [
                {
                    "name": "Peanut butter",
                    "upc": 1234,
                    "cost": 2.29,
                    "category": "food",
                    "on_hand": 4
                },
                ...
            ]
    RETURNS:
        dict: A dictionary where the product name matches to its details:
            {
                "Peanut butter": {
                    "name": "Peanut butter",
                    "upc": 1234,
                    "cost": 2.29,
                    "category": "food",
                    "on_hand": 4
                },
                ...
            }
    """
    inventory_dict = dict() # The dictionary we will return

    # =============================================================================================
    # Checking if a product name is within a list is inefficent because we need to iterate
    # the list for each product we want to check. Instead, if we convert the list of products
    # to a dictionary, we can instantly do membership checking for all future checks.

    # TODO 5: `for` loop through the `inventory` and for each `product` add an item to
    # `inventory_dict` where the key is the product name (Ex: "Peanut Butter") and the
    # value is the `product` dictionary. (See doc string of function for example).
    # (2-3 lines) [Slide]
    # Once done, scroll down for TODO 6.
    # =============================================================================================




    return inventory_dict

# =============================================================================================
# TODO 6: Write a function similar to the one above (`inventory_dict_to_list`) but does the
# reverse action. i.e. Given a dictionary
# (which at some point was outputted by `inventory_list_to_dict`) turn it back
# into its list of dicts representation. (Function name should be `inventory_dict_to_list`)
# (~2-30 lines) [slide 34, 38 & reference TODO 5]
# HINT: to `append` and element to a list, we can call its `append()` method:
#   Example: my_list.append(new_val)
# =============================================================================================





def main():
    grocery_list = {
        'Peanut Butter': 2,
    }
    items_purchased, amount_billed = go_buy_products(grocery_list)
    print(
        f"{sum(items_purchased.values())} products purchased"
        f" for a grand total of ${amount_billed}."
    )
    print(json.dumps(items_purchased, indent=2))

if __name__ == '__main__':
    main()


# Further your skills by trying the following tasks:
#   1) What happens if the inventory within store_info.json contains duplicate product names?
#           Can you raise an exception if this happens or fix it through other means?
#           [slide 17 may be useful]. Any exception can be manually raised with:
#               `raise EXCEPTION_NAME(CUSTOM_MSG)`
#           Where:
#               EXCEPTION_NAME: A valid exception such as RunetimeError:
#                   https://docs.python.org/3/library/exceptions.html#base-classes
#               CUSTOM_MSG: A string for why the error is being raised.
#           Example:
#               `raise ValueError("An unexpected value was found!")`
#               
#   2) Could you add a function that, when invoked, dumps the inventory items into a csv file?
#   3) Could you add a function that will print out all products for a given `category`?
#   4) Can you create a function that will append a string to the end of the `data/logs.txt`
#      file, and then invoke that function throughout your code as a form of logging?
#      Logging is keeping a record of all data input, processes, data output,
#      and final results in a program. Basically its kinda like adding `print`s throughout
#      your code to explain what is happening but saving those prints to a file so you can
#      come back in the future and see what your program did.
#      [slide 38, 43, 45 may be useful]
