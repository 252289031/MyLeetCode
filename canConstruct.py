# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 00:02:42 2018

@author: Administrator
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote)>len(magazine):
            return False
        magazine=list(magazine)
        for s in ransomNote:
            if s not in magazine:
                return False
            else:
                magazine.remove(s)
        return True

d=Solution()


print(d.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi")  ) 
print(d.canConstruct("", "b")  )
print(d.canConstruct("aa", "ab")  )
print(d.canConstruct("fffbfg","effjfggbffjdgbjjhhdegh"))
print(d.canConstruct("", "b")  )   
print(d.canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj") )
print(d.canConstruct("bcjefgecda", "hfebdiicigfjahdddiahdajhaidbdgjihdbhgfbbccfdfggdcacccaebh") )
