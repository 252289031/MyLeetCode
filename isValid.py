# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 00:25:28 2018

@author: Administrator
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst=['(',')','[',']','{','}']
        for i in range(len(lst)):
            print(ord(lst[i]))
        count=0
        if len(lst)==0:
            return False
        if lst[0] not in lst[::2]:
            return False
        for i in range(len(lst)-1):
            if ord(lst[i+1])-ord(lst[i])>=2:
                count+=1
                print(count)
            else:
                count-=0
        if count>=1:
            return True
        
            
            
d=Solution()
print(d.isValid('()[]{}('))
            