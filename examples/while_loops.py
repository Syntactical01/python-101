"""
Example code to show how to convert repative code into a `while`
loop.
"""
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Normally you don't fail this many times, but I want to show
# all the ways something can go wrong.

# ===================================================================
# The naive solution
print("Squared values [0, 5] but not 2^2 because thats boring")
print("Approach A")
print(0**2)
print(1**2)
print(3**2)
print(4**2)
print(5**2)
print("Done A")
# Output numbers: 0, 1, 9, 16, 25

# ===================================================================
# Rewritten, but invalid because we don't skip the `2`.
print("Approach B")
i = 0
while i <= 5:
    print(i**2)
    i += 1 # This is equivalent to i = i + 1 (other options include `-=`, `*=`, `/=`, `**=`)
print("Done B")
# Output numbers: 0, 1, 4, 9, 16, 25

# ===================================================================
# Rewritten using `break`, wrong output amd early abortion.

print("Approach C")
i = 0
while i <= 5:
    print(i**2)
    if i == 2:
        break
    i += 1
print("Done C")
# Output numbers: 0, 1, 4

# ===================================================================
# Rewritten using `continue`, but this gives an infinite loop,
# so its commented out. Use Ctrl + C to abort.

# print("Approach D")
# i = 0
# while i <= 5:
#     print(i**2)
#     if i == 2:
#         continue
#     i += 1
# print("Done D")
# # Output numbers: 0, 1, 4, 4, 4, 4, 4, 4, 4, ....

# ===================================================================
# Cool, so lets fix the infinite loop, but we have the same issue as
# approach B.
print("Approach E")
i = 0
while i <= 5:
    print(i**2)
    i += 1
    if i == 2:
        continue
print("Done E")
# Output numbers: 0, 1, 4, 9, 16, 25

# ===================================================================
# Do the continue before the print, now we are off by one.
print("Approach F")
i = 0
while i <= 5:
    i += 1
    if i == 2:
        continue
    print(i**2)
print("Done F")
# Output numbers: 1, 4, 9, 16, 25, 36

# ===================================================================
# Fix off by one issue, many ways you could have done this.

print("Approach G")
i = 0
while i <= 5:
    if i == 2:
        i += 1
        continue
    else:
        print(i**2)
        i += 1
print("Done G")
# Output numbers: 1, 9, 16, 25, 36

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # =================================================================================================
i = 0
while i < 10:
    print(f"Value of `i` is: {i}")
    i += 1
print(f"Loop has finished, the value of `i` is: {i}")
# # =================================================================================================

# # =================================================================================================
# # Breaking out of a for loop.

# # Two ways to write this loop:
val = input("Input `True` or `False`: ")
while not (val == 'True' or val == 'False'):
    val = input("Input `True` or `False`: ")
print("Freedom!")
# or with a break
while True:
    val = input("Input `True` or `False`: ")
    if val == 'True' or val == 'False':
        break
print("Freedom!")

# # =================================================================================================

while True:
    # Note that we aren't checking if the age is a positive value
    age = input("Please enter your age: ")
    try:
        age = int(age)
        break
    except ValueError:
        print("Invalid age. Please enter a number.")


# # =================================================================================================