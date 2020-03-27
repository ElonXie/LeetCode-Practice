#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
# https://leetcode-cn.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (52.11%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    13K
# Total Submissions: 24.9K
# Testcase Example:  '[1,2,2,3,1]'
#
# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
# 
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
# 
# 示例 1:
# 
# 
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释: 
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
# 
# 
# 示例 2:
# 
# 
# 输入: [1,2,2,3,1,4,2]
# 输出: 6
# 
# 
# 注意:
# 
# 
# nums.length 在1到50,000区间范围内。
# nums[i] 是一个在0到49,999范围内的整数。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 先找度和众数
        # 再算众数的index差值
        # 返回最小差值
        bucket = [0] * 50000
        max_p = -1
        for num in nums:
            bucket[num] += 1
            max_p = max(bucket[num],max_p)
        if max_p ==1:
            return 1
        max_p_num = []
        for i in range(len(bucket)):
            if bucket[i]==max_p:
                max_p_num.append(i)
        res = float('inf')
        while max_p_num:
            same = 0
            min_happen = 0
            max_happen = 0
            cur_max_num = max_p_num.pop()
            for i in range(len(nums)):
                if nums[i]==cur_max_num:
                    if not same:
                        min_happen = i
                    if same==max_p -1:
                        max_happen = i
                    same += 1
            res = min(max_happen-min_happen+1,res)
        return res
        
        
        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.findShortestSubArray([1,2,2,3,1])