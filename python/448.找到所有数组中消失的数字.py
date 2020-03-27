#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (56.50%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    27.3K
# Total Submissions: 48.3K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
# 
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
# 
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
# 
# 示例:
# 
# 
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [5,6]
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)         
        # for num in nums:
        #     index = num if num>0 else num+n
        #     nums[index-1] = nums[index-1] - n if nums[index-1]>0 else nums[index-1]
        # ans = []
        # for index,num in enumerate(nums):
        #     if num>0:
        #         ans.append(index+1)
        # return ans

        for i in range(len(nums)):
                
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative 
            # thus indicating that the number nums[i] has 
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
                
        return result    
# @lc code=end

