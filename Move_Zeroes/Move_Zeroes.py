#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:28:53 2020

@author: hanzhuo
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #sort the array first
        nums.sort();
        i = 0;
        result = 0;
        while i < len(nums):
            print
