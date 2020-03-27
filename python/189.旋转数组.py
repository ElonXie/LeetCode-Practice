#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (40.54%)
# Likes:    497
# Dislikes: 0
# Total Accepted:    100.1K
# Total Submissions: 247K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 
# 说明:
# 
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 法1: 我也不知道这是啥
        # for _ in range(k):
        #     nums.insert(0,nums.pop())
        
        # 法2: 环状替代
        # 计数法
        k = k%len(nums)
        count = 0
        if not k:
            return
        while count<len(nums):
            for i in range(k):
                index = i
                index2 = (index+k)%len(nums)
                # print(index2,index)
                if index2==index:
                    count+=1
                    # print(count,len(nums))
                    break
                tmp = nums[index]
                while index2 != i:
                    tmp,nums[index2] = nums[index2],tmp
                    # print(nums)
                    index = index2
                    index2 = (index2+k)%len(nums)
                    count += 1
                nums[index2] = tmp
                # print(nums)
                count += 1
                if count==len(nums): 
                    break
        
        # 法3: 三次反转
        
# @lc code=end

