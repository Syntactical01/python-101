# Python immutables:
# integer, float, string, tuple, bool, frozenset

# Python mutables
# list, dict, set

# =======================================================================================

# Lets create two variables (labels) which reference an integerobject
# (box) with the value 0
immutable_int = zero = 0

# zero and immutable_int point to the same box (object)
# Note: checking `id` equality (==) and just using `is` does the same thing.
# `==` and `is` are not equivalent. Don't be fooled.
# `is` asks if the labels point to the same box.
# `==` asks if the boxes value are equal. (Notice 'some' overlap)
print(id(immutable_int) == id(zero), immutable_int is zero) # True True
print(f"{immutable_int=} {zero=}") # immutable_int=0 zero=0 <-- Self documenting format strings

# The value within the box though is immutable (a safe) so by incrementing it,
# we actually make a new object (box) and reference that new box.
immutable_int += 1 

# So these no longer point to the same object (two different boex).
print(id(immutable_int) == id(zero)) # False
print(f"{immutable_int=} {zero=}") # immutable_int=1 zero=0

# =======================================================================================

# Now lets looks at a list, which is mutable
# Create two variables which reference the same empty list object, this object is mutable, (no list)
mutable_list = new_list = list()

# They reference the same object
print(id(mutable_list) == id(new_list)) # True
print(f"{mutable_list=} {new_list=}") # mutable_list=[] new_list=[]

mutable_list += [1, 2, 3]

print(id(mutable_list) == id(new_list)) # True
print(f"{mutable_list=} {new_list=}") # mutable_list=[1, 2, 3] new_list=[1, 2, 3]

