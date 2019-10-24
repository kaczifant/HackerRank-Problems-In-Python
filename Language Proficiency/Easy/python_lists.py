# https://www.hackerrank.com/challenges/python-lists/problem?h_r=profile

'''
Consider a list (list = []). You can perform the following commands:

	1. insert i e: Insert integer e at position i.
	2. print: Print the list.
	3. remove e: Delete the first occurrence of integer e.
	4. append e: Insert integer e at the end of the list.
	5. sort: Sort the list.
	6. pop: Pop the last element from the list.
	7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands 
where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
'''

if __name__ == '__main__':

    N = int(input())
    l = []
	
	# Enter your code below
    commands = []

    for i in range(N):
        commands.append(input().split())

    for command in commands:
        if command[0] == "insert":
            l.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(l)
        elif command[0] == "remove":
            l.remove(int(command[1]))
        elif command[0] == "append":
            l.append(int(command[1]))
        elif command[0] == "sort":
            l.sort()
        elif command[0] == "pop":
            l.pop()
        elif command[0] == "reverse":
            l.reverse()

