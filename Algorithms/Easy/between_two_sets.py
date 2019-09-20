# https://www.hackerrank.com/challenges/between-two-sets/problem?h_r=profile

#!/bin/python3

import functools
import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    between1 = []
    a.sort()
    b.sort()
    
    x = min(b) // max(a)
    for i in range(1, x+1):
        between1.append(max(a) * i)      
      
    exclude1 = set()
    for i in range(len(between1)):
        for j in range(len(a)):
            if between1[i] % a[j] != 0:
                exclude1.add(between1[i])
        
    between2 = list(set(between1).difference(exclude1))   
  
    exclude2 = set()
    
    for i in range(len(between2)):
        for j in range(len(b)):
            if b[j] % between2[i] != 0:
                exclude2.add(between2[i])
    
    between3 = set(between2).difference(exclude2)  
    return len(between3)
        
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

