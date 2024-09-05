import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    players = ['Louise', 'Richard']
    player_number = 0

    # Find a two base number
    # decrement that val from n
    # Whomever reaches 1 first win
    found_two_base_number = False
    for i in range(n, 0, -1):
        import pdb; pdb.set_trace()
        if bin(i).count("1") == 1:
            # print(f"Here is f: {i} and here is {players[player_number]}")
            n -= i
            if i == 1:
                return players[player_number]
            player_number = 1 if player_number == 0 else 0
            next
    
    # import pdb; pdb.set_trace()
    return players[player_number]



def counterGame(n):
    set_bits = bin(n-1).count('1')
    if set_bits % 2 == 1:
        return 'Louise'
    else:
        return 'Richard'


print(counterGame(132))# == 'Louise')
# print(counterGame(1560834904) == 'Richard')
# print(counterGame(6) == 'Richard')