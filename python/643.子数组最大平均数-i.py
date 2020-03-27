#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (38.12%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 31.9K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
# 
# 示例 1:
# 
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# 
# 注意:
# 
# 
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。
# 
# 
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 典型滑动窗口?
        avg = 0
        for i in range(k):
            avg += nums[i]
        avg /= k
        max_avg = avg
        if len(nums)==k:
            return max_avg
        for i in range(0,len(nums)-k):
            avg += (nums[i+k]-nums[i])/k
            max_avg = max(avg,max_avg)
        return max_avg
# @lc code=end

