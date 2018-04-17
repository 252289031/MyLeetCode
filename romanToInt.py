# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 21:43:56 2018

@author: Administrator
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=0
        for i in range(0,len(s)-1):
            if dict[s[i]]<dict[s[i+1]]:
                result -= dict[s[i]]
            else:
                result+=dict[s[i]]
        return result+dict[s[-1]]
                   
        
d=Solution()
if d.romanToInt("III")==3:
    print("pass")
else:
    print("fail")
if d.romanToInt("IV")==4:
    print("pass")
else:
    print("fail")
if d.romanToInt("IX")==9:
    print("pass")
else:
    print("fail")
if d.romanToInt("LVIII")==58:
    print("pass")
else:
    print("fail")
if d.romanToInt("MCMXCIV")==1994:
    print("pass")
else:
    print("fail")