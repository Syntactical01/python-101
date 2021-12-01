"""
Code used by the PowerPoint to show variable assignment and the imporance
of proper variable names.
"""

# During variable assignment, the right hand side is fully evaluated
# before the left.
var1 = 1 + 2 # 3: addition
my_age = 2021 - 1997 # 24: subtraction
aprox_age_in_days = my_age * 365 # 8760: multiplication
_TWO_CUBED = 2 ** 3 # 8: exponents
TWO_SQUARED = _TWO_CUBED / 2 # 4: division
floor_division = 367 // 100 # 3: round down division OR floored division
modulus = 367 % 100 # 67: modulus OR remainder of a division
var1 += TWO_SQUARED + 23 # 29: Same as var1 = var1 + TWO_SQUARED + 23
var1 -= var1 # 0: Same as var1 = var1 - var1
# Others: *=, **=, /=, //=, %=


# Variable naming is important
# Everyone loves accronyms and short names but avoid them...
# Which is easier to understand?
au = ['John', 'Jane']
u = 'Rick'
if u in au:
    print('OK')
else:
    print('Not OK')

# or
authorized_users = ['John', 'Jane']
current_user = 'Rick'
if current_user in authorized_users:
    print('This user is authorized.')
else:
    print('This user is not  authorized.')


# Though you should strive to avoid really long variable names
wizard_of_oz_character_names = [
    'The Tin Man',
    'Dorothy Gale',
    'Scarecrow',
    'The Cowardly Lion'
]
# Alternatives
characters = [ # Characters in the wizard of oz
]
woz_characters = [ # Characters in the wizard of oz
]
character_names = [ # Characters in the wizard of oz
]

# but DO NOT do:
c = [ # Characters in the wizard of oz
]
chars = [ # Characters in the wizard of oz

]

# Variables are just tags that point to objects. These are discussed more in detail later in the presentation.