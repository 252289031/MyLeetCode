# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:19:59 2018

@author: Administrator
"""

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a==b:
            return -1
        if len(a)>len(b):
            a,b=b,a
        ac=len(a)
        bc=len(b)
        for i in range(-1,-len(a),-1):
           if a[i]==b[:len(a)][i]:
               ac-=1
        print(ac)
        print(a,b)
        return ac
        
        
        
d=Solution()
if d.findLUSlength("aba","cdc") == 3:
    print(True)
else:
    print(False)
    
if d.findLUSlength("abaaaa","cdc") == 3:
    print(True)
else:
    print(False)

if d.findLUSlength("aefawfawfawfaw","aefawfeawfwafwaef") == 17:
    print(True)
else:
    print(False)