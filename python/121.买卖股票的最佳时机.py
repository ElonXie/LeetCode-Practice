#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        sum = 0
        for index in range(len(prices)-1):
            profit = prices[index+1] - prices[index]
            if profit>=0:
                sum += profit
            else:
                max_profit = max(sum,max_profit)
                if profit+sum<0:
                    sum = 0
                else:
                    sum += profit
        max_profit = max(sum,max_profit)
        return max_profit
# @lc code=end

