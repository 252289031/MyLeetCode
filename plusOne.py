# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 12:01:39 2018

@author: Administrator
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        print(digits,end='')
        digits.reverse()
        digits[0]=digits[0]+1
        for i in range(0,len(digits)):
            j=i+1
            if digits[i]==10:
               digits[i] =0
               if i==len(digits)-1:
                   digits.append(1)
               else:
                   digits[j] +=1
        digits.reverse()
        return digits
    

s=Solution()
digits=[1,2,3]
print("Result =",s.plusOne(digits))

digits=[4,3,2,1]
print("Result =",s.plusOne(digits))

digits=[9]
print("Result =",s.plusOne(digits))

digits=[9,9]
print("Result =",s.plusOne(digits))
digits=[9,9,9]
print("Result =",s.plusOne(digits))
digits=[8,9,9,9]
print("Result =",s.plusOne(digits))
digits=[8,8,9,9]
print("Result =",s.plusOne(digits))