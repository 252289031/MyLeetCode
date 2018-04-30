# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:43:00 2018

@author: Administrator
"""
import copy
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        rl=copy.deepcopy(matrix)
        l=len(matrix)
        for i in range(l):
            for j in range(l):
                print(l-1-j,i)
                matrix[i][j]=rl[l-1-j][i]
        
              
matrix =\
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
'''[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]'''
#print(matrix)
s=Solution()
s.rotate(matrix)
print(matrix)