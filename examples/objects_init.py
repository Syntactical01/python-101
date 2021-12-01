# A 100% scripted game.

player_1 = "banana"
player_2 = 11
player_3 = [12, 18,
            player_1,
            player_2]

print(isinstance(player_1, int), '\n')

print(isinstance(player_1, str), '\n')

print(player_1, '\n')

print(player_1[::-1], '\n')

print(player_1 == player_2, '\n')

try: 
    print(player_2[::-1], '\n')
except Exception as err:
    print(err, '\n')

print(isinstance(player_2, str), '\n')

print(isinstance(player_2, int), '\n')

print(player_2 + 7, '\n')

print(player_3[0], '\n')

print(player_3[1], '\n')

print(player_3[2][::-1], '\n')

print(player_3[2] is player_1, '\n')

try: 
    print(player_3[3][::-1], '\n')
except Exception as err:
    print(err, '\n')

print(player_3[3] is player_2)

# Now swap out all the players with objects.

