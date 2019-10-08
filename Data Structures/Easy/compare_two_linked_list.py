# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

#!/bin/python3

import os
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

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):

    current_a = llist1
    current_b = llist2

    while current_a or current_b:
        if current_a is None or current_b is None:
            return 0
        elif current_a.data == current_b.data:
            current_a = current_a.next
            current_b = current_b.next
        else:
            return 0   

    return 1

if __name__ == '__main__':