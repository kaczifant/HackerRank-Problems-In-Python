# https://www.hackerrank.com/challenges/itertools-product/problem

'''
You are given a two lists A and B. Your task is to compute their cartesian product A * B.
'''

from itertools import product

if __name__ == "__main__":

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    prod = list(product(a, b))
    
    for pair in prod:
        print(pair, end=' ')