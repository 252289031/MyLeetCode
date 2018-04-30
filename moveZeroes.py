# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:17:10 2018

@author: Administrator
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        for i in nums:
            if i ==0:
                nums.remove(i)
                nums.append(0)'''
        count=0
        for i in range(-len(nums),-1,1):
            print(i,nums[i])
            if nums[i]==0:
                nums.pop(i)
                count+=1
        for i in range(count):
            nums.append(0)
        
        
        
        
        
        
        
        
        
        
        
#nums=[2,3,1,4,6]        
#print(nums.pop(3),nums)    
d=Solution()        
nums =[4,2,4,0,0,3,0,5,1,0]
d.moveZeroes(nums)
print(nums)