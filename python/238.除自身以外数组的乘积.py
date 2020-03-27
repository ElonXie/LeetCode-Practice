#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
# https://leetcode-cn.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (66.46%)
# Likes:    323
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 45.1K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i]
# 之外其余各元素的乘积。
# 
# 
# 
# 示例:
# 
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 
# 
# 
# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
# 
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
# 
#
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # 以下解法1 O(1) O(N)
        # L,R = [1]*len(nums),[1]*len(nums)
        # for i in range(0, len(nums)-1):
        #     L[i+1] = L[i]*nums[i]
        # for j in range(len(nums)-2,-1,-1):
        #     R[j] = R[j+1]*nums[j+1]
        # ans = [] 
        # for i in range(0,len(nums)):
        #     ans.append(L[i]*R[i])
        # return ans

        # 以下为解法2
        ans = [1]*len(nums)
        for i in range(0,len(nums)-1):
            ans[i+1] = ans[i]*nums[i]
        curPro = 1
        for i in range(len(nums)-2,-1,-1):
            curPro *= nums[i+1]
            ans[i] *= curPro
        return ans

# @lc code=end

