# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

'''
Complete the height function. It must return the height of a binary tree as an integer.

Height has the following parameter(s):
	- root: a reference to the root of a binary tree.
Note -The Height of binary tree with single node is taken as zero.
'''

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):

    if root is None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)
