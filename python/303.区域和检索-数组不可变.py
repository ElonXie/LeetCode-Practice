#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
# https://leetcode-cn.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (60.59%)
# Likes:    145
# Dislikes: 0
# Total Accepted:    33.6K
# Total Submissions: 55.2K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
  #'[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# 
# 示例：
# 
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 说明:
# 
# 
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。
# 
# 
#
from typing import List
# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.dp = [0] * len(nums)
        if nums:
            self.dp[0] = nums[0]
            for i in range(1,len(nums)):
                self.dp[i] = self.dp[i-1]+nums[i]
        
    

    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.dp[j]
        return self.dp[j]-self.dp[i-1] 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

if __name__ == '__main__':
        nums = [-2,0, 3, -5, 2, -1]
        s = NumArray(nums)
        print(s.sumRange(0,5))

