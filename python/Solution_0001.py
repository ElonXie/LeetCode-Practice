# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:51:56 2020

@author: e
"""

class Solution:
    def twoSum(self,nums,target):
        dic = dict()
        for index,num in enumerate(nums):
            if (target-num in dic):
                return [dic[target-num],index]
            dic[num] = index
        return None


if __name__=='__main__':
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    ans = s.twoSum(nums,target)
    print(ans)
            
    
            
            