# https://www.hackerrank.com/challenges/plus-minus/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    pos, neg, zero = 0, 0, 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    print('%1.6f' %(pos/length))
    print('%1.6f' %(neg/length))
    print('%1.6f' %(zero/length))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
