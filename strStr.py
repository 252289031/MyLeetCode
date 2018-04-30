# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:33:38 2018

@author: Administrator
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
#        if len(haystack)==0 and len(needle)==0:
#            return -1
        return haystack.find(needle)
        
        
        
        
        
        
        
d=Solution()
        
haystack = "hello"
needle = "ll"
print(d.strStr(haystack,needle))
haystack = "aaaaa"
needle = "bba"
print(d.strStr(haystack,needle))
print(d.strStr("",""))
print(d.strStr("asdgb",""))