# https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):

    dist = []

    for i in range(len(s)-1):
        dist.append(abs(ord(s[i]) - ord(s[i+1])))

    if dist == list(reversed(dist)):
        return 'Funny'
    else:
        return 'Not Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
