# https://www.hackerrank.com/challenges/staircase/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    space = n - 1
    pound = 1
    for row in range(n):
        print(" " * space + '#' * pound)
        space -= 1
        pound += 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
