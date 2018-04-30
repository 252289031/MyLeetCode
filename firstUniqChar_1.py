# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:18:29 2018

@author: Administrator
"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(ch) for ch in letters if s.count(ch)==1]
        print(min(index) if len(index)>0 else -1)
#        l=len(s)
#        for i in range(l):
#            if s[:i].find(s[i])==-1 and s[i+1:].find(s[i])==-1:
#                return i
#        return -1



d=Solution()

s = "aadadaad"
print(s,'====',d.firstUniqChar(s))
s = "loveleetcode"
print(s,'====',d.firstUniqChar(s))
s = "cc"
print(s,'====',d.firstUniqChar(s))
s = "z"
print(s,'====',d.firstUniqChar(s))

print("dddccdbba=========",d.firstUniqChar("dddccdbba"))