# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:51:56 2018

@author: Administrator
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=['a','o','e','i','u','A','O','E','I','U']
        d=[]
        for i,t in enumerate(s):
            if t in a:
                d.append(i)
        l=len(d)//2
        s=list(s)
        print(s,d)
        for i in range(l):
            s[d[i]] ,s[d[len(d)-i-1]]=s[d[len(d)-i-1]],s[d[i]]
        return ''.join([x for x in s])
        
d=Solution()
if d.reverseVowels("hello")=="holle":
    print("Pass")
else:
    print("False")
if d.reverseVowels("leetcode")=="leotcede":
    print("Pass")
else:
    print("False")
if d.reverseVowels("aA")=="Aa":
    print("Pass")
else:
    print("False")