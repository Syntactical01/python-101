current_year = 2020
date_of_birth = 1983
print(f"I was born on {date_of_birth} so I am {current_year - date_of_birth} years old.")

print(f"2^4 + 3 is {2**4 + 3}")

name = input("Please enter your name: ")
age = input(f"Hello {name}, how old are you: ")
age = int(age)
response = f"You are {age}, that means you were born in ~{current_year - age}"
print(response)

