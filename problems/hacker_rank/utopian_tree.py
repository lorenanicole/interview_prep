#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    is_spring = True
    height = 1

    for cycle in range(n):
        if is_spring:
            height *= 2
            is_spring = False
        else:
            height += 1
            is_spring = True
        # print(f"Here is height {height} for epoch {n}")
    return height

print(utopianTree(5) == 14)