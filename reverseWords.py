# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:52:21 2018

@author: Administrator
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
# =============================================================================
#         i,j=0,0
#         while i<len(s):
#             if s[i]==" ":
#                 result+=(s[j:i].strip())[::-1]
#                 j=i
#                 result+=" "
#             if i==len(s)-1:
#                 result+=(s[j:].strip())[::-1]
#             i+=1
#         result=" "
# =============================================================================
        return " ".join(r[::-1] for r in s.split(" "))
    
    
    
d=Solution()
print(d.reverseWords("Let's take LeetCode contest"))