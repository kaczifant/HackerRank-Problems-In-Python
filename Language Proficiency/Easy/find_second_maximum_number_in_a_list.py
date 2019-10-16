# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given n scores. 
Store them in a list and find the score of the runner-up.
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


	# Write your code here
	
    s = set(arr)
    unique_list = list(s)
    unique_list.sort()

    print(unique_list[-2])

