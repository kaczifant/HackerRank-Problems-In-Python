# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):

    if not (head1 or head2):
        return

    if not head1:
        return head2
    if not head2:
        return head1
    
    current_a = head1
    current_b = head2
    smallest = None

    if head1.data <= head2.data:
        head_merged = head1
        smallest = current_a
        current_a = smallest.next
    else:
        head_merged = head2
        smallest = current_b
        current_b = smallest.next
    
    while current_a and current_b:
        if current_a.data <= current_b.data:
            smallest.next = current_a
            smallest = current_a
            current_a = smallest.next            
        else:
            smallest.next = current_b
            smallest = current_b
            current_b = smallest.next
           
    if not current_a:
        smallest.next = current_b

    if not current_b:
        smallest.next = current_a

    return head_merged


if __name__ == '__main__':