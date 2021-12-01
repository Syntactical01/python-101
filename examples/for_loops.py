# Initial Example

i = 0
items = ["name", 2, 3.1, 4, True, None]
while i < len(items):
    if isinstance(items[i], (int, float)):
        print(items[i] * 10)
    else:
        print(items[i])
    i += 1



# How to rewrite code to conform to a `for` loop
for value in ["name", 2, 3.1, 4, True, None]:
    if isinstance(value, (int, float)):
        print(value * 10)
    else:
        print(value)


# NOTE: Note the repition below. This implies we can refactor
# our code in such a way that we don't repeat ourselved.
numbers = []
amount_to_enter = 3
print(f"Enter {amount_to_enter} numbers.")

first_number = input("Enter the 1 number: ")
numbers.append(float(first_number))

second_number = input("Enter the 2 number: ")
numbers.append(float(second_number))

third_number = input("Enter the 3 number: ")
numbers.append(float(third_number))

print(numbers)

numbers = []
amount_to_enter = 3
print(f"Enter {amount_to_enter} numbers.")
for number in range(amount_to_enter): # 0-based indexing.
    input_number = input(f"Enter the {number + 1} number: ")
    numbers.append(float(input_number))
print(numbers)

numbers = []
amount_to_enter = int(input("How many numbers do you want to enter? "))
print(f"Enter {amount_to_enter} numbers.")
for number in range(amount_to_enter): # 0-based indexing.
    input_number = input(f"Enter the {number + 1} number: ")
    numbers.append(float(input_number))
print(numbers)



# NOTE: Loops can be nested, the code along problem does this.

pasta_recipes = [
    ["Spaghetti", "Marinara", "Pork", "Carrots"],
    ["Farfalle", "Roasted Tomato", "Beef", "Mushrooms"],
    ["Penne", "Alfredo", "Chicken", None],
    ["Penne", "Alfredo", "Chicken", None, "Mushrooms"],
]

# If we find a mushroom, lets abort
# Without breaks, we want to print all lists that contain mushrooms.

print("============")
for index, ingredients in enumerate(pasta_recipes):
    print(f"Checking ingredients {index}")
    mushrooms_discovered = False
    for ingredient in ingredients:
        if ingredient == "Mushrooms":
            print("WARNING: This ingredient is mushrooms. ₙₐₛₜᵧ")
            mushrooms_discovered = True
    if mushrooms_discovered:
        print("Ingredients contains mushrooms: ", ingredients)

# With breaks, we only care if one list contains mushrooms.
print("============")
for index, ingredients in enumerate(pasta_recipes):
    print(f"Checking ingredients {index}")
    mushrooms_discovered = False
    for ingredient in ingredients:
        if ingredient == "Mushrooms":
            print("WARNING: This ingredient is mushrooms. ₙₐₛₜᵧ")
            mushrooms_discovered = True
            break # Short circuit the inner for loop
    if mushrooms_discovered:
        print("Ingredients contains mushrooms: ", ingredients)
        break # Short circuit outer loop
print("============")
# Or we can use continue as a way to print all ingredients that aren't mushrooms
for index, ingredients in enumerate(pasta_recipes):
    for ingredient in ingredients:
        if ingredient == "Mushrooms":
            continue
        print(ingredient, end=" ") # By default print uses `end="\n"`
    print() # Equivalent to print(end='\n') || print('\n', end="")
