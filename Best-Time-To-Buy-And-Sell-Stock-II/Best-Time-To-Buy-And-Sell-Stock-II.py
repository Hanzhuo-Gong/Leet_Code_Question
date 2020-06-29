class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxProfit = 0
        i = 1
        while i < len(prices):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
            i +=1
        
        return maxProfit
        

# The question is very tricky, I initially thought I need to write an algorithm to maximum the profit. 
# Can use Simple One Pass which add up the profits while looping over the list.The result is the same
