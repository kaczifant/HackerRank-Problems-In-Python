# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = []
    i = 0
    if len(c) == 2:
        return 1
    while i != len(c)-1 and i != len(c)-2:
        if not c[i+2]:
            i += 2
        else:
            i += 1
        steps.append(i)
     
    if not c[-2] and c[-3]:
        steps.append(len(c)-1)
    
    return len(steps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
