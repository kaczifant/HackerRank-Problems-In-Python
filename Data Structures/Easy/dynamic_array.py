# https://www.hackerrank.com/challenges/dynamic-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    
    seqList = [[] for x in range(n)]
    lastAnswer = 0
    to_print = []
    
    for i in queries:
        q, x, y = i
        index = (x ^ lastAnswer) % n
        if q == 1:
            seqList[index].append(y)   
        elif q == 2:
            size = y % len(seqList[index])
            lastAnswer = seqList[index][size]
            to_print.append(str(lastAnswer))

    return to_print    
           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
