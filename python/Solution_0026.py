# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:03:02 2020

@author: e
"""

class Solution:
    def removeDuplicates(self,nums):
        i = 0
        for j,num in enumerate(nums):
            if num != nums[i]:
                i += 1
                nums[i] = num
        return i+1

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,1,2]
    len_1 = s.removeDuplicates(nums1)
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    len_2 = s.removeDuplicates(nums2)
    print(len_1)
    print(len_2)
    print(nums1[:len_1])
    print(nums2[:len_2])
