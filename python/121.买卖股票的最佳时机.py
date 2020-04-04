#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        # dp : 状态 {手里有票. 手里没票, 买入次数(0,1)}  动作{买入,卖出,不动}
        dp_have = -prices[0]
        dp_no = 0
        for i in range(1,len(prices)):
            dp_have,dp_no = max(dp_have,-prices[i]),max(dp_have+prices[i],dp_no)
        return dp_no

    # def maxProfit(self, prices: List[int]) -> int:
    #     max_profit = 0
    #     sum = 0
    #     for index in range(len(prices)-1):
    #         profit = prices[index+1] - prices[index]
    #         if profit>=0:
    #             sum += profit
    #         else:
    #             max_profit = max(sum,max_profit)
    #             if profit+sum<0:
    #                 sum = 0
    #             else:
    #                 sum += profit
    #     max_profit = max(sum,max_profit)
    #     return max_profit
# @lc code=end

