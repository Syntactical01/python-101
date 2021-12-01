
# If statement example
state = 'Minnesota'

if state == 'Minnesota':
    print("Go Vikings, maybe one day you'll win a super bowl.")
elif state == 'Wisconsin':
    print("Go Pack Go!")
elif state == 'Illinois':
    print(''.join(chr(int(char, 2)) for char in [
        '0b1000110', '0b101010', '0b101010',
        '0b1101011', '0b100000', '0b1100100',
        '0b1100001', '0b100000', '0b1100010',
        '0b1100101', '0b1100001', '0b1110010',
        '0b1110011'])) # Super secret message...
else:
    print("Irrelevant.")


# If statement condition examples
my_name = "John C. Smith"
if my_name:
    print(my_name)
if len(my_name) > 3:
    print(f"{my_name} is longer then 3 characters.")
if 'Smith' in my_name:
    print(f"'Smith' is contained within '{my_name}'")
if '.' not in my_name:
    print(f"'.' is not contained within '{my_name}'")
if my_name.endswith('Smith') and my_name.startswith('John'):
    print("The name starts with John and ends with Smith.")

# Ternary Example

# If nothing is inputted then an empty
# string is returned.
input_name = input("Please enter your name: ")
# Empty strings are considered Falsey
name = input_name if input_name else "[No Name Entered]"
print(name)

