# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 21:54:09 2018

@author: Administrator
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        if len(nums) >=2:
            for i in range(len(nums)-1):
                #print("num[{0}]={1}".format(i,nums[i]))
                #print("num[{0}]={1}".format(i+1,nums[i+1]))
                if nums[i]==nums[i+1]:
                    return True
        return False
d=Solution()
nums=[3,1]
print(d.containsDuplicate(nums))

nums=[1,1,2,3,4,5,6,7]
print(d.containsDuplicate(nums))
nums=[1,1,2,2,4,4,7,7]
print(d.containsDuplicate(nums))
nums=[2,14,18,22,22]
print(d.containsDuplicate(nums))
nums=[1,2,3,1]
print(d.containsDuplicate(nums))
nums=[2,14,18,22,22]
#print(d.containsDuplicate(nums))
print(set(nums))