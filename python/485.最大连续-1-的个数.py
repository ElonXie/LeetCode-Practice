#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (55.76%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    28.9K
# Total Submissions: 51.9K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
# 
# 示例 1:
# 
# 
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 
# 
# 注意：
# 
# 
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                # Increment the count of 1's by one.
                count += 1
            else:
                # Find the maximum till now.
                max_count = max(max_count, count)
                # Reset count of 1.
                count = 0
        return max(max_count, count)
    # return max(map(len, ''.join(map(str, nums)).split('0')))

# @lc code=end

