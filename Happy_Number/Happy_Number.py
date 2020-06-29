#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:53:57 2020

@author: hanzhuo
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numberSet = set()
        while n != 1:
            temp = 0
            for i in str(n):
                temp += int(i) **2  
            n = temp  
            if n not in numberSet:
                numberSet.add(n)
            else:
                return False
        return True
    
#ob1 = Solution()
#print(ob1.isHappy(19))

#I intially thought to put the result in a list a loop the list, later find out
#a easy step by just using casting.


#can also use the shortcut sum(int(i)**2 for i in str(n)) for shorter line