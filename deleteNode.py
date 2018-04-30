# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 22:33:00 2018

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
        
        
        
d=ListNode()
d=(1,2,3,4)
s=Solution(d)
s.deleteNode(3)
        