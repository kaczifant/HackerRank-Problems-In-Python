# https://www.hackerrank.com/challenges/array-left-rotation/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def left_rotation(a, d):

    d = d % len(a) if d > len(a) else d
    rot_arr = a[d:] + a[:d]
    return rot_arr

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = left_rotation(a, d)
	
    for item in result:
        print(item, end=' ')
