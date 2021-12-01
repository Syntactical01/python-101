

example_lst = [95, 55, 99, 83, 19, 85, 58, 1, 51, 9]
print(f'The largest element in the list is: {max(example_lst)}')

# `max` is a built-in function but I could implement my own version that works
# "simularly":
def custom_max(iterable: list, key=None, foobar=None):
    """
    Return the max value within an iterable.
    If the iterable is empty, a ValueError will be raised.
    """
    print(f"Foobar value: {foobar=}")
    if key:
        raise NotImplementedError("`key` is not yet implemented.")
    max_val = None
    for item in iterable:
        if max_val == None or item > max_val:
            max_val = item
    if max_val is None:
        raise ValueError("Iterable is empty.")
    return max_val

# I can invoke a funtion via:
example_lst = [95, 55, 99, 83, 19, 85, 58, 1, 51, 9]

max_val = custom_max(example_lst)


# OR
max_val = custom_max(iterable=example_lst)



example_lst = [95, 55, 99, 83, 19, 85, 58, 1, 51, 9]
# =============================================================
# The following are all technically equivalent.

# Variable arguments only.
max_val = custom_max(example_lst, None, 3)
print(max_val)

# First argument is variable, second two are keyword (and flopped).
max_val = custom_max(example_lst, foobar=3, key=None)
print(max_val)

# Keyword arguments only, but order is the same as the definition.
max_val = custom_max(iterable=example_lst, key=None, foobar=3)
print(max_val)

# Keyword arguments only, but order is shuffled from the definition
max_val = custom_max(key=None, iterable=example_lst, foobar=3)
print(max_val)

# =============================================================



# OR

# The second (variable) spot would be the key.
try:
    max_val = custom_max(example_lst, 2) # This will raise the NotImplementedError
except NotImplementedError:
    print("Not implemented exception was thrown.")


print(f'The largest element in the list is: {max_val}')
