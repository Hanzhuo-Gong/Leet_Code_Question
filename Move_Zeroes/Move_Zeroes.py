#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:28:53 2020

@author: hanzhuo
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        totalLength = len(nums)
        while i < totalLength:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                totalLength = totalLength - 1
            else:
                i += 1
