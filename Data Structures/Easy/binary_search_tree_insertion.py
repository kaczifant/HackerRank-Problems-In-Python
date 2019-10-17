# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

'''
You are given a pointer to the root of a binary search tree and values to be inserted into the tree.
Insert the values into their appropriate position in the binary search tree 
and return the root of the updated binary tree. 
'''

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

# Complete the function below

    def insert(self, val):
        
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, curr_node, val):
        
        if val < curr_node.info:
            if curr_node.left is None:
                curr_node.left = Node(val)
            else:
                self._insert(curr_node.left, val)
        elif val > curr_node.info:
            if curr_node.right is None:
                curr_node.right = Node(val)
            else:
                self._insert(curr_node.right, val) 
        else:
            print("Number already present.")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
