# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:05:55 2020

@author: e
"""

'''
    与最大和子序列题目是类似的.只是这里不是数字求和,是利润求和.
    但是这个题目里就不会有那个憨憨的小于0也要return了.这题小于0就return0
    思路:
        
'''

class Solution:
    def maxProfit(self,prices):
        max_sum = 0
        sum = 0
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            if profit >= 0:
               sum = max(sum,0)+profit 
            else:
                sum+=profit
            max_sum = max(max_sum,sum)
        return max_sum
    
if __name__ == '__main__':
    s = Solution()
#    prices = [7,1,5,3,6,4]
    prices = [7,6,4,3,1]
#    prices = [1,2]
    profit = s.maxProfit(prices)
    print(profit)