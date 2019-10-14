# https://www.hackerrank.com/challenges/pangrams/problem

#!/bin/python3

import math
import os
import random
import re
import string
import sys

# Complete the pangrams function below.
def pangrams(s):

    letters = set(string.ascii_lowercase)
    s = set(s.lower())
    if letters <= s:
         return "pangram"
    else:
        return "not pangram"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
