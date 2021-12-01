my_info = {} # || dict()
my_info["age"] = 12
my_info["eye_color"] = "green"
my_info[42] = "The answer to life."

print(my_info, '\n')

print(my_info[42], '\n')

print("eye_color" in my_info, '\n')

print("height" in my_info, '\n')

print(12 in my_info, '\n')


# Dictionaries are created using {} or dict()

my_dict = {}
# or
my_dict = dict()

# Lists use [] to get items at a given index
my_list = ['a', 'b', 'c']
print(my_list[1])

# Dictionaries also use [] to get items, but instead of an index, it wants a key.
# The left side of the : is the key, the right is the value:
my_dict = {
    1: 2,
    "foo": "bar",
    (1, 2): [3, 4, 5]
}
print(my_dict["foo"])
print(my_dict["1"])
try:
    print(my_dict["333"])
except KeyError:
    print("Dictionary did not contain this key.")

# We can also add/overwrite values with a simular notation
my_dict["333"] = "A new val" # Add a new value
my_dict[1] = 3 # Overwrite an existing value

# Checking to see if a key is in a dictionary:
if "333" in my_dict:
    print("The above key is inside te dictionary.")
if None in my_dict:
    print("None is not in the dictionary.")

# When we iterate over a dictionary, we iterate over its keys.
# But we can use .values() & .items()
for key in my_dict:
    print(f"{key=}")

for key, val in my_dict.items():
    print(f"{key=} {val=}")

for val in my_dict.values():
    print(f"{val=}")

# Dictionaries are good for storing data.
# list approacj
my_data = [
    [-8, 12.8],
    [10.2, 11.3],
    [2.4, 12.4],
]

# Dictionary approach
my_data = [ # The number is now clearer
    {"min_temp": -8, "max_temp": 12.8, "metadata": {"unit": "\u00B0"}},
    {"min_temp": 10.2, "max_temp": 11.3, "metadata": {"unit": "\u00B0"}},
    {"min_temp": 2.4, "max_temp": 12.4},
]
# Dictionaries are also a lot easier to store in files. (JSON with Python)

# This makes my data cleaner and the code can become a little cleaner (debatable)
cur_temp = 4
for datum in my_data:
    # the `if __ in ___` is instance unlike a list lookup.
    unit = datum["metadata"]["unit"] if "metadata" in datum else ""
    min_temp, max_temp = datum["min_temp"], datum["max_temp"]
    if  min_temp <= cur_temp <= max_temp:
        print(f"Temperature ({cur_temp}{unit}) is within range ({min_temp}{unit} - {max_temp}{unit})")
    