# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:40:46 2018

@author: Administrator
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y=str(abs(x))
        y=int(y[::-1])
        if x <0:
            if -y<-2147483648 :
                return 0
            else:
                return -y
        else:
            if y>2147483648 :
                return 0
            else:
                return y

a=Solution()
print(a.reverse(123))
print(a.reverse(-123))
print(a.reverse(1534236469))
print(a.reverse(-1534236469))
            
            
            
            
            
        