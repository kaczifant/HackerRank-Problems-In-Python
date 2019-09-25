# https://www.hackerrank.com/challenges/alternating-characters/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    count = 0
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            count += 1
        i += 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
