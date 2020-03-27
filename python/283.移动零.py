#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (59.57%)
# Likes:    502
# Dislikes: 0
# Total Accepted:    111K
# Total Submissions: 186.2K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 显然是正向遍历可以更少移动.遇到0后,将0计数为N,至遇到下一个0前,
        # 所有后边的数都往前N个,遇到0 N++, 至 最后一个数,然后把倒N个变成0
        zeros = 0
        for index,num in enumerate(nums):
            if not num:
                zeros += 1
                continue
            else:
                nums[index] = 0
                nums[index-zeros] = num
                
        # 慢指针指向当前最后, 快指针指向一下个数, 两指针中间的是 0
        # 每次快指针遇到数,就和慢指针swap,两个各++
        # 快指针遇到0, 快指针++        
        
# @lc code=end

