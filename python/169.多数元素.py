#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 哈希表:
        dic = dict()
        max_count = 0
        max_num = None
        for index,num in enumerate(nums):
            dic[num] = dic[num]+1 if num in dic else 1
            if dic[num] > max_count:
                max_num, max_count = num, dic[num]
        return max_num
    
        # 有一种正负抵消的办法.假设某数是众数,计value=1,其余数value=-1,
        # 则 sum > 0
        # 于是计第一个数value为1,前N序列求和至sum=0,再计第N+1 value=1
        # 此算法 T:O(1) S:O(1)
        
        # 还可用分治法 T:O(nlgn) S:O(lgn)
    
# @lc code=end

