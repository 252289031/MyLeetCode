# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 20:15:20 2018

@author: Administrator
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''if len(nums1)<len(nums2):
            max_mun=nums2
            min_num=nums1
        elif len(nums1) ==0 or len(nums2) ==0:
            return []
        else:
            max_mun=nums1
            min_num=nums2
        index=0
        arr=[]
        max_mun.sort()
        min_num.sort()
        for i ,t in enumerate(min_num):
            print(i,"----",t) 
            if t in max_mun[index:]:
                arr.append(t)
                index=max_mun.index(t)+1
                continue
        return arr'''
        arr=[]
        if len(nums1)==0 or len(nums2)==0:
            return []
        if len(nums2)<len(nums1):
            nums1,nums2=nums2,nums1
        for i in nums1:
            if i in nums2:
                arr.append(i)
                nums2.remove(i)
        return arr
         
        
        
        
        
    
d=Solution()     
nums1 = [1, 2]
nums2 = [2, 1]
print('reslut = ',d.intersect(nums1,nums2))   
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print('reslut = ',d.intersect(nums1,nums2))
nums1 = [1, 2, 4, 5,5]
nums2 = [5,5]
print('reslut = ',d.intersect(nums1,nums2))
nums1 = [1,2]
nums2 = [1,1]
print('reslut = ',d.intersect(nums1,nums2))
nums1 = [1,1]
nums2 = [1,2]
print('reslut = ',d.intersect(nums1,nums2))