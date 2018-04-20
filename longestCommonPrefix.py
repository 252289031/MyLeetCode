# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:43:59 2018

@author: Administrator
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        '''
        #Method one
        if len(strs)==0:
            return ""
        min_str=strs[0]
        min_len=len(strs[0])
        for i in strs:
            if len(i)<min_len:
                min_str=i
                min_len=len(i)
        for i in strs:
            j=0
            count=0
            while j!=len(i) and j!=len(min_str):
                if i[j]==min_str[j]:
                    count+=1
                else:
                    break
                j+=1
            min_str=min_str[:count]
        return min_str
        for i,t in enumerate(zip(*strs)):
            print(i,t)
            print(strs[i])'''
        #methon two
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for others in strs:
                if others[i] != ch:
                    return shortest[:i]
        return shortest


            
            
            
            
            
d=Solution()
print(d.longestCommonPrefix(["flower","flow","flight"]))
#d.longestCommonPrefix(["dog","racecar","car"])