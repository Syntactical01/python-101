# Example of what a list can contain
my_list = ['John', 'Jane', 0.3, 12, True, [0, 1, 2]]
one_element_lst = [12]


example_lst = [95, 55, 99, 83, 19, 85, 58, 1, 51, 9]
print(f'Original list: {example_lst}')
print(f'The length of the list is {len(example_lst)}')
print(f'The largest element in the list is: {max(example_lst)}')
print(f'The smallest element in the list is: {min(example_lst)}')
print(f'The element at the front of the list is: {example_lst[0]}')
print(f'The element at the back of the list is: {example_lst[-1]}')
print(f'The list in sorted order is: {sorted(example_lst)}')
# Note that `sorted()` does not change the list it sorted
# so:
print(example_lst) # Will output: [95, 55, 99, 83, 19, 85, 58, 1, 51, 9]
# but if I use `.sort()` it will sort the list in place thus changing the initial list:
example_lst.sort()
print(example_lst) # Output: [1, 9, 19, 51, 55, 58, 83, 85, 95, 99]

# So if you want the sorted version of a list but don't want to change the original do:
sorted_lst = sorted(example_lst)

# Note that `.sort()` returns `None` so you can't oneline it like this:
print(example_lst.sort()) # Output: None
# ^ you must two line this if you wish to do an inplace sort
# or you can use `sorted`:
print(sorted(example_lst)) # Output: [1, 9, 19, 51, 55, 58, 83, 85, 95, 99]

# If you do not  understand the the `.some_method()` notation yet, please
# read the examples about classes.
