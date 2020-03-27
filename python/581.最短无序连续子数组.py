#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (34.03%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 55.7K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
#
#
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
#
# 说明 :
#
#
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。
#
#
#
from typing import List
# @lc code=start


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 即左数组为升序,右数组也升序.且三个数组符合
        # max(left)<=min(middle)<max(middle)<=min(right)
        # 从左扫描至非升序,从右扫描至非升序,且时刻存储最值
        # 中间即为一个非升序的最小数组.求这个数组的最小值和最大值
        # 如果双边取等号,就可以输出了.
        # 如果取不到两个不等号.则逆向重新倒退(或者从dic查) 复杂度的问题了
        # left_end = 0
        # right_start = len(nums)-1

        # while left_end < len(nums)-1:
        #     if nums[left_end] > nums[left_end+1]:
        #         break
        #     left_end += 1
        # while right_start > left_end:
        #     if nums[right_start] < nums[right_start-1]:
        #         break
        #     right_start -= 1
        # if left_end == right_start:
        #     return 0
        # left_end -= 1
        # right_start += 1

        # middle_min = nums[left_end+1]
        # middle_max = nums[left_end+1]
        # for index in range(left_end+1, right_start):
        #     middle_min = min(middle_min, nums[index])
        #     middle_max = max(middle_max, nums[index])
        # while left_end >= 0:
        #     # if nums[left_end] <= min(middle_min, nums[left_end+1]):
        #     if nums[left_end] <= middle_min:
        #         break
        #     left_end -= 1
        #     # middle_max = max(middle_max, nums[left_end+1])
        #     # middle_min = min(middle_min, nums[left_end+1])
        # while right_start <= len(nums)-1:
        #     # if nums[right_start] >= max(nums[right_start-1], middle_max):
        #     if nums[right_start] >= middle_max:
        #         break
        #     right_start += 1
        # return right_start-left_end-1

        length = len(nums)
        if length <= 1:
            return 0
        high, low = 0, length-1
        max_num, min_num = nums[0], nums[length-1]
        for index in range(length):
            max_num = max(max_num, nums[index])
            min_num = min(min_num, nums[length-index-1])
            if nums[index] < max_num:
                high = index
            if nums[length-index-1] > min_num:
                low = length-index-1
        ans = high-low+1 if high > low else 0
        return ans

        # for index in range(0, len(nums)-1):
        #     if nums[index] > nums[index+1]:
        #         left_end = index
        #         break
        # if left_end == -1:
        #     return 0
        # for index in range(len(nums)-1, left_end, -1):
        #     if nums[index] < nums[index-1]:
        #         right_start = index
        #         break
        # if (nums[right_start] >= nums[left_end]) and (right_start-left_end == 1):
        #     return 0
        # elif nums[right_start] < nums[left_end]:

        # # elif right_start-left_end == 1:
        # #     # 错pan了,必须各让一个出来,因为这两个数本身就互相没顺序.
        # #     # 但是会触到边界,咋办呢,没事,直接搞到边界就好了嘛
        # #     # if left_end > 0:
        # #     #     left_end -= 1
        # #     #     middle_min = middle_max = nums[left_end+1]
        # #     #     if right_start != len(nums)-1:
        # #     #         right_start += 1
        # #     #         middle_min = middle_max = nums[right_start-1]
        # #     # elif right_start != len(nums)-1:
        # #     #     right_start += 1
        # #     #     middle_min = middle_max = nums[right_start-1]
        # #     # else:
        # #     #     return 2
        # #     if len(nums) == 1:
        # #         return 2
        # #     else:
        # #         middle_max, middle_min = nums[left_end], nums[right_start]
        # #         left_end -= 1
        # #         right_start += 1

        # # else:
        # #     # if nums[right_start] < nums[left_end] :
        # #     #     while right_start<len(nums):
        # #     #         if nums[right_start] < nums[left_end]:
        # #     #             right_start += 1
        # #     #     if right_start==len(nums):
        # #     #         while left_end>0:
        # #     #             if nums[right_start-1]<nums[left_end]:
        # #     #                 left_end -= 1

        # #     middle_min = nums[left_end+1]
        # #     middle_max = nums[left_end+1]
        # for index in range(left_end+1, right_start):
        #     middle_min = min(middle_min, nums[index])
        #     middle_max = max(middle_max, nums[index])
        # while left_end >= 0:
        #     if nums[left_end] <= min(middle_min, nums[left_end+1]):
        #         break
        #     left_end -= 1
        #     middle_max = max(middle_max, nums[left_end+1])
        #     middle_min = min(middle_min, nums[left_end+1])
        # while right_start <= len(nums)-1:
        #     if nums[right_start] >= max(nums[right_start-1], middle_max):
        #         break
        #     right_start += 1

        # # for index in range(left_end, -1, -1):
        # #     if nums[index] <= min(middle_min, nums[index+1]):
        # #         left_end = index
        # #         break
        # # for index in range(right_start, len(nums)):
        # #     if nums[index] >= max(nums[index-1], middle_max):
        # #         right_start = index
        # #         break
        # return right_start-left_end-1

        # @lc code=end


if __name__ == "__main__":
    s = Solution()
    # nums = [5, 4, 3, 2, 1]
    # nums = [2, 1, 1, 1, 1]
    # nums = [2, 3, 3, 2, 4]
    # nums = [1, 2, 4, 5, 3]
    # nums = [1, 3, 5, 4, 2]
    ans = s.findUnsortedSubarray(nums)
    print(ans)


# 思路应该是,左侧有序,右侧有序,且左侧的最右侧数,小于等于右侧最左数
# 然后 对中间求最值,并逐步将左侧左推,右侧右推
