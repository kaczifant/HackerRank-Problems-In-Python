# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
        
    if position == 0:  
        node.next = head
        head = node
    else:
        current_node = head
        current_node_pos = 0
        
        while position-1 != current_node_pos:
            current_node = current_node.next
            current_node_pos += 1
        
        node.next = current_node.next
        current_node.next = node

    return head

if __name__ == '__main__':