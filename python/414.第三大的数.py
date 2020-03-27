#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# https://leetcode-cn.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (34.34%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    19.9K
# Total Submissions: 57.9K
# Testcase Example:  '[3,2,1]'
#
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
#
# 示例 1:
#
#
# 输入: [3, 2, 1]
#
# 输出: 1
#
# 解释: 第三大的数是 1.
#
#
# 示例 2:
#
#
# 输入: [1, 2]
#
# 输出: 2
#
# 解释: 第三大的数不存在, 所以返回最大的数 2 .
#
#
# 示例 3:
#
#
# 输入: [2, 2, 3, 1]
#
# 输出: 1
#
# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。
#
#
#
from typing import List
# @lc code=start


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 1.暴力法
        first = second = third = -1000000000000
        count = 0
        for index, num in enumerate(nums):
            if num > first:
                second, third = first, second
                first = num
                count += 1
                print('first:{},second:{},third:{}'.format(first, second, third))
            elif num < first and num >= second:
                if num != second:
                    third = second
                    count += 1
                second = num
                print('first:{},second:{},third:{}'.format(first, second, third))
            elif num < second and num >= third:
                count += 1
                third = num
                print('first:{},second:{},third:{}'.format(first, second, third))
        if count >= 3:
            return third
        else:
            return first

        # 2.用堆栈如何?
        # num<[-1]. len<3时,直接放末尾
        # num>[-1] 如果len=3,pop,再比
        # num>[-1], len<3, 则排序三个数
        ans = list()
        ans.append(nums[0])
        for num in nums:
            if num>ans[0]:
                ans = [num] + ans
            elif (len(ans)>1 and num>ans[1]) or (len(ans)==1):
                ans = [ans[0]] + [num] + ans
            elif (len(ans)>2 and num>ans[2]) or (len(ans)==2):
                ans = ans[0:2] + [num]
            if len(ans)>3:
                ans.pop()
        if len(ans)==3:
            return ans[-1]
        else:
            return ans[0]
            
            
            
        #     if num < ans[-1] and len(ans) < 3:
        #         ans.append(num)
        #     elif num > ans[-1] and len(ans) == 3:
        #         if num != ans[0] and num != ans[1]:
        #             ans.pop()
        #             if num>ans[0]:
        #                 ans = num + ans
        #             elif num>ans[1]:
        #                 ans[1],ans[2] = num,ans[1]
        #             else:
        #                 ans.append(num)
        #     elif num>ans[-1] and len(ans)<3:
        #         ans = num + ans
        # if len(ans)==3:
        #     return ans[2]
        # else:
        #     return ans[0]

        
        
        # 以下为比较好的代码:
        # class Solution:
        # def thirdMax(self, nums: List[int]) -> int:
        # first = second = third = float('-inf')
        # for num in nums:
        #     if num > third:  # 通过第3关
        #         if num < second:
        #             third = num
        #         elif num > second:  # 通过第2关
        #             if num < first:
        #                 third = second
        #                 second = num
        #             elif num > first:  # 通过第1关
        #                 third = second
        #                 second = first
        #                 first = num
        # if third == float('-inf'):
        #     return first
        # else:
        #     return third

        
        
if __name__ == '__main__':
    nums = [1, 2, 2, 5, 3, 5]
    s = Solution()
    print(s.thirdMax(nums))
# @lc code=end
