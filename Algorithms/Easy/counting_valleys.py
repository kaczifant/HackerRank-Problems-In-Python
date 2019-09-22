# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

from itertools import accumulate
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    route = []
    for i in s:
        if i == 'U':
            route.append(1)
        else:
            route.append(-1) 
    
    steps = list(accumulate(route, lambda x,y: x+y))
    
    # Converting [0, -1, -2, -1, 0] into '0 -1 -2 -1 0' 
    steps_str = ''
    for i in steps:
        steps_str += str(i) + ' ' # space is important otherwise -10 and -1 0 will be the same
    valley = steps_str.count('-1 0')  # we only have to count the end of the valley
   
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
