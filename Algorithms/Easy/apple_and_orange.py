# https://www.hackerrank.com/challenges/apple-and-orange/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_pos = list(map(lambda x: x+a, apples))
    oranges_pos = list(map(lambda x: x+b, oranges))
    
    def within_range(arr):
        fruit_in_range = 0
        for fruit in arr:
            if fruit >= s and fruit <= t:
                fruit_in_range += 1
        return fruit_in_range
            
    print(within_range(apples_pos))
    print(within_range(oranges_pos))
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
