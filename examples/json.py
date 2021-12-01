# Imports import objects from the ether.

# Python has a lot of code that is useful but not always used so Python will not include it by default.
# To import this code that is hidden but we want to use we use `import`

# Built In
import json

# Imports can also import objects from other files which we will get into a little later.

# json is an object which contains a lot of methods we can use while working with JSON.


example_data = [
    {
        1: 1
    },
    {
        "some_key": {
            "val1": [1, 2, 3],
            "val2": True,
            "val3": None
        }
    },
]
print(example_data)

print("\n------------------------------\n")

json_data = json.dumps(example_data, indent=4)
print(type(json_data))
print(json_data)

print("\n------------------------------\n")

json_data = json.loads(json_data)
print(type(json_data))
print(json_data)
print(json_data[1]['some_key']['val2'])


# Above we used:
#   dumps(dict || list): Dump JSON to string (dumpString)
#   loads(str): Load JSON from string (loadString)

# When working with files, there are two similar functions:
#   dump(dict || list, file_obj):
#   load(file_obj)

example_data = [
    {
        1: 1
    },
    {
        "some_key": {
            "val1": [1, 2, 3],
            "val2": True,
            "val3": None
        }
    },
]
print(example_data)

print("\n------------------------------\n")

with open('json_save.json', 'w+') as file_obj:
    json.dump(example_data, file_obj, indent=4)
    print("File Written.")

print("\n------------------------------\n")

with open('json_save.json', 'r') as file_obj:
    # The load will raise an exception if the JSON is invalid.
    json_data = json.load(file_obj)
print(type(json_data))
print(json_data)
print(json_data[1]['some_key']['val2'])

