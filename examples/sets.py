print([1, 2, 3, 3, 4, 5, 5], '\n')

print((1, 2, 3, 3, 4, 5, 5), '\n')

print({1, 2, 3, 3, 4, 5, 5}, '\n')

strings = "foo", "bar", "dilly"
print(set(strings))


# To create a new set, we must explicity set it
my_set = set()
# my_set = {} would actually create a dictionary not a set.
# I am gonna code golf to make this look cleaner.
# Please DO NOT do this in your code:
my_set.add(1); print(my_set)
my_set.add(2); print(my_set)
my_set.add(3); print(my_set)
my_set.add(2); print(my_set)
my_set.remove(2); print(my_set)