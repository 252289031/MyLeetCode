# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 19:29:11 2018

@author: Administrator
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count("A")>1 or s.count("LLL")>0:
            return False
        return True
        
        
        
d=Solution()
if d.checkRecord("PPALLP")==True:
    print("Pass")
else:
    print("False")
if d.checkRecord("PPALLL")==True:
    print("Pass")
else:
    print("False")    