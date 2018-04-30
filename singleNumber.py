# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 18:57:35 2018

@author: Administrator
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result=0
        for i in nums:
           result=i^result
        return result
        
               
d=Solution()
'''nums=[1,0,1]

print(nums,"Result",d.singleNumber(nums))
nums=[2,2,1]
print(nums,"Result",d.singleNumber(nums))'''
nums=[4,1,2,1,2] 
print(nums,"Result",d.singleNumber(nums))    
nums=[1]
print(nums,"Result",d.singleNumber(nums))
nums=[1,1,2,2,3,4,4]
print(nums,"Result",d.singleNumber(nums))
nums=[1,1,2,2,3,3,4]
print(nums,"Result",d.singleNumber(nums))