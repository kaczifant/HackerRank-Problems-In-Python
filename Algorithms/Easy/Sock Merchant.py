# https://www.hackerrank.com/challenges/sock-merchant/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    if len(ar) == len(set(ar)):
        return pairs
    else: 
        unique = False
        i = 0
        while not unique:
            num = ar[i]
            index_num = ar.index(num)
            num_occ = ar.count(num)
            num_pair = num_occ//2
            if num_pair == 0:
                i += 1
            else:
                pairs += num_pair
                for i in range(num_pair * 2):
                    ar.remove(num)
                    n -= 1
                i = index_num
                if len(ar) == len(set(ar)):
                    unique = True
        return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
