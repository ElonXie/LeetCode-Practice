#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (37.73%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    35.1K
# Total Submissions: 93K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j
# 的差的绝对值最大为 k。
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 
# 示例 2:
# 
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 
# 示例 3:
# 
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
# 
#
from typing import List
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        
        # dic = dict()
        # for index,num in enumerate(nums):
        #     if num not in dic:
        #         dic[num] = index
        #     else:
        #         #print(index)
        #         #print(dic[num])
        #         if index-dic[num]>k:
        #             dic[num] = index
        #         else:
        #             return True
        # return False
        
        windows = set()
        for i in range(len(nums)):
            if nums[i] in windows:
                return True
            windows.add(nums[i])
            if len(windows) > k:
                windows.remove(nums[i-k])
        return False
        
        # dic = dict()
        # max_distance = 0
        # for index,num in enumerate(nums):
        #     if num not in dic:
        #         dic[num] = index
        #     else:
        #         max_distance = max(max_distance,index-dic[num])
        # print(max_distant)
        # return max_distance<=k
        
        ### 这个题目有问题: 题意是 有重复元素,且重复元素索引绝对值不超过k
        ### 实际上: 存在索引差小于等于k的重复元素即返回
        
        
if __name__ =='__main__':
    s = Solution()
    nums = [1,0,1,1]
    k = 1
    print(s.containsNearbyDuplicate(nums,k))
    
# @lc code=end

