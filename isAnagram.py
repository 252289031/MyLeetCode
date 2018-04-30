# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:18:29 2018

@author: Administrator
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s==t:
            print('1')
            return True    
        else:
            s=list(s)
            s.sort()
            t=list(t)
            t.sort()
            if s==t:
                print('12')
                return True
            else:
                return False
d=Solution()
s = "a"
t = "b"
print(d.isAnagram(s,t))




#s = "aadadaad"
#print(d.firstUniqChar(s))
#s = "loveleetcode"
#print(d.firstUniqChar(s))
#s = "cc"
#print(d.firstUniqChar(s))