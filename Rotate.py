# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:12:00 2018

@author: Administrator
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        if k<l and k>0:
            remine=l-k
            for i in range(0,remine):
                nums.append(nums[i])
            del nums[0:len(nums)-remine-k]
            return 1
                
b=Solution()        
nums=[1,2,3]
b.rotate(nums,0)
if nums== [1,2,3]:
    print("Pass")
else:
    print("Fail")
    
nums=[1,2,3,4,5,6,7]
b.rotate(nums,3)
if nums== [5,6,7,1,2,3,4]:
    print("Pass")
else:
    print("Fail")
    
nums=[1,2,3,4,5,6,7]
b.rotate(nums,1)
if nums== [7,1,2,3,4,5,6]:
    print("Pass")
else:
    print("Fail")
    
nums=[1,2,3,4,5,6,7]
b.rotate(nums,6)
if nums== [2,3,4,5,6,7,1]:
    print("Pass")
else:
    print("Fail")
    
    
nums=[1,2,3,4,5,6,7]
b.rotate(nums,7)
if nums== [1,2,3,4,5,6,7]:
    print("Pass")
else:
    print("Fail")


