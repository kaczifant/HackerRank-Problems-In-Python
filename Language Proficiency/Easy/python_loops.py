# https://www.hackerrank.com/challenges/python-loops/problem

'''
Read an integer N. For all non-negative integers i < N, print the i squared.
'''

if __name__ == '__main__':
    n = int(input())

	# Write your code below
	
    for i in range(n):
        print(i**2)
