# https://www.hackerrank.com/challenges/list-comprehensions/problem

'''
You are given three integers X, Y and Z representing the dimensions of a cuboid along 
with an integer N. You have to print a list of all possible coordinates given by (i,j,k)
on a 3D grid where the sum of i+j+k is not equal to N.
Here, 0 <= i <= X, 0 <= j <= Y, 0 <= k <= Z.
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
	
	# Write your code below
	
    l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(l)

