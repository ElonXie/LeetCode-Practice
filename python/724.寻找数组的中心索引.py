#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#
# https://leetcode-cn.com/problems/find-pivot-index/description/
#
# algorithms
# Easy (36.53%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    32.2K
# Total Submissions: 88.2K
# Testcase Example:  '[1,7,3,6,5,6]'
#
# 给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
# 
# 我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
# 
# 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
# 
# 示例 1:
# 
# 
# 输入: 
# nums = [1, 7, 3, 6, 5, 6]
# 输出: 3
# 解释: 
# 索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
# 同时, 3 也是第一个符合要求的中心索引。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# nums = [1, 2, 3]
# 输出: -1
# 解释: 
# 数组中不存在满足此条件的中心索引。
# 
# 说明:
# 
# 
# nums 的长度范围为 [0, 10000]。
# 任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if not nums:
            return -1
        res_right = -nums[0]
        for num in nums:
            res_right += num
        res_left = 0
        for i in range(len(nums)-1):
            if res_left==res_right:
                return i
            res_left += nums[i]
            res_right -= nums[i+1]
        if res_left==res_right:
            return -1
        return -1
# @lc code=end


if __name__ == '__main__':
    s = Solution()