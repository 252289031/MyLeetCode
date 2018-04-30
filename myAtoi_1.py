# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 22:31:35 2018

@author: Administrator
"""

class Solution:
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        arr=['1','2','3','4','5','6','7','8','9','0','.']
        alpha='qazwsxedcrfvtgbyhnujmikolp'
        smybol=""
        result=""
        r=0
        if len(string)==0 or string[0] in alpha:
            return 0
        for i in range(len(string)):
            if string[i] == "-" or string[i]=="+":
                smybol=string[i]
            elif string[i] in arr:
                result=result+string[i]
            else:
                result=result+","
        p=max(result.split(','),key=len)
        if len(p) !=0:
            r= int(p)
        else:
            return 0
        if smybol=="-":
            r=-r
        if r < -2147483648 :
            return 2147483648
        elif r >2147483647:
            return 2147483647
        else:
            return r
                
                
d=Solution()
string=""
print(d.myAtoi(string))

string="+"
print(d.myAtoi(string))

string="   -42"
print(d.myAtoi(string))

string="-91283472332"
print(d.myAtoi(string))

print(d.myAtoi("   3.142596"))
print(d.myAtoi("words and 987"))