'''找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
 

限制：

2 <= n <= 100000
'''
from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        index = 0
        while index<len(nums):
            num = nums[index]
            if num==index:
                index += 1 
                continue
            elif num == nums[num]:
                return num
            else:
                nums[index],nums[num] = nums[num],num

        return None

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,1,0,2,5,3]
    print(s.findRepeatNumber(nums))

