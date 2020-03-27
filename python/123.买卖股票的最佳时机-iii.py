#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            首先,最大子序列之和,肯定是比最大单笔多的.但并不一定比最大两个单笔多
            因此,前两个最大子序列之和,才比两个最大单笔多.
            但是并不一定有两个最大子序列.
            所以需要判断是否存在两个最大子序列.--> 这很复杂
            我们维护四个值:单笔最大,单笔第二大.子序列最大.子序列第二大.
            
            维护一个max,一个second_max
        '''
        max_profit = 0
        second_profit = 0
        cur_profit = 0
        for index in range(len(prices)-1):
            profit = prices[index+1] - prices[index]
            if profit>=0:
                cur_profit += profit
            else:
                if profit+cur_profit>=0
            
            
            
            if profit>=max_profit:
                max_profit,second_profit = profit,max_profit
            elif profit<max_profit and profit>=second_profit:
                second_profit = profit
        return max_profit+second_profit
# @lc code=end

