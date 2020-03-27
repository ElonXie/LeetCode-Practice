#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (76.48%)
# Likes:    483
# Dislikes: 0
# Total Accepted:    64.3K
# Total Submissions: 84K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            全排列/组合/子集问题,很相似,并且可以用通用策略
            首先,解空间很大:
                全排列 : N!
                组合 : N!
                子集 : 2^N (每个元素都有存在和不存在两种状态)
            为了保证指数级解法的结果完整且无冗余.常用三种方法:
                递归
                回溯
                基于二进制掩码和对应位掩码之间的映射字典生成排序/组合/子集            
        '''

        # 首先考虑嵌套循环,但是嵌套循环复杂度太高了.
        # 嵌套循环不能实现,在于每次的内循环的层数跟当前的length_array有关
        # 考虑递归
        output = [[]]
        for num in nums:
            output += [curr+[num] for curr in output]
        return output

        # 字典法
        # def backtrack(first=0, curr=[]):
        #         # if the combination is done
        #     if len(curr) == k:
        #         output.append(curr[:])
        #     for i in range(first, n):
        #         # add nums[i] into the current combination
        #         curr.append(nums[i])
        #         # use next integers to complete the combination
        #         backtrack(i + 1, curr)
        #         # backtrack
        #         curr.pop()

        # output = []
        # n = len(nums)
        # for k in range(n + 1):
        #     backtrack()
        # return output

# @lc code=end
