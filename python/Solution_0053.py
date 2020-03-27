# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:29:55 2020

@author: e
"""

'''
    这道题主要是节点上的问题比较误导人.
    思路:
        1. 分治法(没仔细看)
        2. 模拟法(本方法)
        3. 动态规划(没仔细看)
'''


class Solution:
    def maxSubArray(self,nums):
        sum = 0
        max_sum = nums[0]
        #整体思路是对的,但是要考虑节点问题
        #每次遇到负数都是节点
        #遇到正数直接
            #
        for i,num in enumerate(nums):
            if num>=0:
                sum = max(sum,0)+num
                max_sum = max(max_sum,sum)
            else:                
                if sum+num > 0:        
                    max_sum = max(max_sum,sum)
                    sum+=num
                else:
                    sum = num
                    max_sum = max(max_sum,sum)
                    
        max_sum = max(max_sum,sum)
        return max_sum
    
if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,-2]
    ans = s.maxSubArray(nums)
    print(ans)
                    
        