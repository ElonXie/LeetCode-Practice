#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            这里不需要是连续子序列求和了
        '''
        sum = 0
        for index in range(len(prices)-1):
           sum += max(prices[index+1]-prices[index],0)
        return sum
# @lc code=end

