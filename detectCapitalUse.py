# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:31:51 2018

@author: Administrator
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
        
        
        
        
d=Solution()
if d.detectCapitalUse("USA")==True:
    print("pass")
else:
    print("Flase")
    
    
if d.detectCapitalUse("FlaG")==True:
    print("pass")
else:
    print("Flase")
    
if d.detectCapitalUse("Google")==True:
    print("pass")
else:
    print("Flase")
    
if d.detectCapitalUse("leetcode")==True:
    print("pass")
else:
    print("Flase")