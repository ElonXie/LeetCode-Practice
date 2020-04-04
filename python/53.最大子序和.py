#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (49.89%)
# Likes:    1781
# Dislikes: 0
# Total Accepted:    193.8K
# Total Submissions: 387.7K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#

# @lc code=start
class Solution:
    '''这题官方题解好乱啊'''
    def maxSubArray(self, nums: List[int]) -> int:
        # 3. 分治法
        # 分治法是什么傻逼做法嗷... 哪里精妙. 你都会cross_sum了. 我就不明白为啥不会贪心

    # def maxSubArray(self, nums: List[int]) -> int:
    #     # 2. DP
    #     dp = [0] * len(nums)
    #     dp[0] = nums[0]
    #     for i in range(1,len(nums)):
    #         if dp[i-1]<=0:
    #             dp[i] = nums[i]
    #         else:
    #             dp[i] = dp[i-1]+nums[i]
    #     return max(dp)

    # def maxSubArray(self, nums: List[int]) -> int:
    #     # 1. 遍历记录最大值
    #     cur_sum = nums[0]
    #     max_sum = nums[0]
    #     for i in range(1,len(nums)):
    #         if cur_sum<=0:
    #             cur_sum = nums[i]
    #         else:
    #             cur_sum += nums[i]
    #         max_sum = max(max_sum,cur_sum)
    #     return max_sum

# @lc code=end

