

my_tuple = ('John', 'Jane', 0.3, 12, True, [0, 1, 2], (0, 1, 2))

# Note that for one element tuples the comma, is needed to tell
# Python that the parathesis are creating a tuple and not just declaring
# order of operation such as: math = (2+2)*2
one_element_tuple = (1,)

# This:
a, b = 1, 2

# Is basically equivalent to this:
_variables = 1, 2
a, b = _variables # This is called tuple unpacking.

# We can also explicitly tupple unpack:
print(_variables) # (1, 2)
print(*_variables) # Equivalent to print(1, 2) -> 1 2



# Many python operations take an iterable (which a tuple is) so
# we can use a tuple very similar to how we used a list:
print(f'Original tuple: {my_tuple}')
print(f'The length of the tuple is {len(my_tuple)}')
print(f'The element at the front of the tuple is: {my_tuple[0]}')
print(f'The element at the back of the tuple is: {my_tuple[-1]}')

# But we can't change the tuple
my_tuple[1] = 'Doe' # TypeError: 'tuple' object does not support item assignment.

# However if one of its objects is mutable, we can tell that object to change itself.
my_tuple[5].append(3) # This will add 3 to the end of the tuple at the 5th index.



