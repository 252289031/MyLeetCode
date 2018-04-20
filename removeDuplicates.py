# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:22:36 2018

@author: Administrator
"""
import datetime
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        arr=nums.copy()
        del nums[:]
        for i in range(len(arr)):
            if arr[i] not in nums:
                nums.append(arr[i])
        '''
        i = 1
        for j in range(len(nums)):
            if nums[i-1] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return len(nums[:i])
        

start = datetime.datetime.now()                   
b=Solution()
nums=[1,1,0,1,2,2,3,3,5,5,6,7,8,9,5]
b.removeDuplicates(nums)
print(nums)
end = datetime.datetime.now()
print((end-start).seconds,"s")