#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (49.37%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    16.3K
# Total Submissions: 33K
# Testcase Example:  '[1,2,3]'
#
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 
# 示例 1:
# 
# 
# 输入: [1,2,3]
# 输出: 6
# 
# 
# 示例 2:
# 
# 
# 输入: [1,2,3,4]
# 输出: 24
# 
# 
# 注意:
# 
# 
# 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 3正/2负1正
        # 3正好找, 2负1正如何处理?
        # 准备5个数就ok了
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        infin = float("inf")
        max_queue = [-infin] *3 
        min_queue = [infin] * 2
        for num in nums:
            if num > max_queue[2]:
                max_queue[2] = num
                if max_queue[2]>max_queue[1]:
                    max_queue[2],max_queue[1] = max_queue[1],max_queue[2]
                if max_queue[1]>max_queue[0]:
                    max_queue[1],max_queue[0] = max_queue[0],max_queue[1]
            if num < min_queue[1]:
                min_queue[1] = num
                if min_queue[1] < min_queue[0]:
                    min_queue[1],min_queue[0] = min_queue[0],min_queue[1]
        max_under_multi = min_queue[0]*min_queue[1]
        max_upper_multi = max_queue[1]*max_queue[2]
        if max_under_multi>max_upper_multi and max_queue[0] >=0:
            return max_under_multi*max_queue[0]
        else:
            return max_upper_multi*max_queue[0]

        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.maximumProduct([1,-2,-3,-4]))