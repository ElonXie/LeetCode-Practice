#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#
# https://leetcode-cn.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (22.10%)
# Likes:    238
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 71.3K
# Testcase Example:  '[4,2,3]'
#
# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
# 
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，总满足 array[i] <= array[i + 1]。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
# 
# 
# 示例 2:
# 
# 输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 
# 
# 
# 
# 说明：
# 
# 
# 1 <= n <= 10 ^ 4
# - 10 ^ 5 <= nums[i] <= 10 ^ 5
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 遇到逆序对[i,i+1]时,先修改 nums[i]=nums[i+1] 如果此时nums[i-1]和nums[i]逆序了
        # 则改成nums[i+1]=nums[i] 进入下一轮
        count = 0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                count += 1
                if count>1:
                    return False
                cur_val = nums[i]
                nums[i] = nums[i+1]
                if (i>0 and nums[i]<nums[i-1]):
                    nums[i] = cur_val
                    nums[i+1] = nums[i]
                    

        return count<=1

if __name__ == '__main__':
    s = Solution()
    s.checkPossibility([4,2,1])
# @lc code=end

