#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (51.66%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    111.7K
# Total Submissions: 216.4K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
# 
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: true
# 
# 示例 2:
# 
# 输入: [1,2,3,4]
# 输出: false
# 
# 示例 3:
# 
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
# 
#
from typing import List
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1. 哈希 T:O(n) S:O(n)
        # 2. 原数组做桶? 好像不行.因为没有size
        # dic = dict()
        # for num in nums:
        #     if num in dic:
        #         return True
        #     dic[num] = 1
        # return False
        
        return len(nums) != len(set(nums))
# @lc code=end

