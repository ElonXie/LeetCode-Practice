#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 除了是排序好的数组以外,和001没有什么区别呀.
        # 有更简单的方法吗?
        # dic = dict()
        # for index,num in enumerate(numbers):
        #     if target-num in dic:
        #         return [dic[target-num],index+1]
        #     else:
        #         dic[num] = index+1
        # return []
        
        low,high = 0,len(numbers)-1
        while low<high:
            sum = numbers[low]+numbers[high]
            # print(sum)
            if numbers[low]+numbers[high]==target:
                return [low+1,high+1]
            elif numbers[low]+numbers[high] < target:
                low += 1
            else:
                high -= 1
        return [-1,-1]
    
    
if __name__ == '__main__':
    numbers = [-3,3,4,90]
    s = Solution()
    print(s.twoSum(numbers,0))
    
# @lc code=end

