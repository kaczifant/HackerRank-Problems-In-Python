# https://www.hackerrank.com/challenges/maximizing-xor/problem

#!/bin/python3

import itertools
import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):

    arr = [x for x in range(l, r+1)]
    xor = []
    combinations = list(itertools.combinations(arr, 2))
    
    for combination in combinations:
        xor.append(combination[0] ^ combination[1])

    return max(xor)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
