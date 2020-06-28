#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 14:56:12 2020

@author: hanzhuo
"""

class Solution(object):
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        noDuplicate = set()
        for i in nums:
            if i in noDuplicate: 
                noDuplicate.remove(i)
            else: 
                noDuplicate.add(i)
        for i in noDuplicate: 
            return i
        
#this quetion can use set, another list, hash function and XOR to solve this easily
#Try not to use while loop here since so many conditional statements will be used.