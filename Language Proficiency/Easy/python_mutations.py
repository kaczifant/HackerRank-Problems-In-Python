# https://www.hackerrank.com/challenges/python-mutations/problem?h_r=profile

'''
Read a given string, change the character at a given index and then print the modified string.
'''

# Complete the function
def mutate_string(string, position, character):

    chars = list(string)
    chars[position] = character
    new_string = ''.join(chars)    
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)