#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        front = 0
        for i,num in enumerate(nums):
            if num!=nums[front]:
                front += 1
                nums[front] = num
        return front+1
                
# @lc code=end

