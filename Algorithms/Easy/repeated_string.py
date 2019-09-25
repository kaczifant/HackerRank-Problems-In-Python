# https://www.hackerrank.com/challenges/repeated-string/problem?h_r=profile

#!/bin/python3

import itertools
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    a_in_s = s.count('a')
    num_a = 0
    
    x = n // len(s)
    num_a += a_in_s * x
   
    remainder = n % len(s)
    if remainder != 0:
        num_a += s[:remainder].count('a')
    
    return num_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
