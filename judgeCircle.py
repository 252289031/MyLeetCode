# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:06:49 2018

@author: Administrator
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d={'R':1,'L':-1,'D':-1,'U':1}
        pos_x ,pos_y=0,0
        for s in moves:
            if s == 'R' or s=='L':
                pos_x+=d[s]
            if s == 'D' or s=='U':
                pos_y+=d[s]
        return True if pos_x==0 and pos_y==0 else False
                
        
        
d=Solution()
print(d.judgeCircle("UD"))
print(d.judgeCircle("LL"))
