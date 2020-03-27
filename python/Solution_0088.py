# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:28:29 2020

@author: e
"""
'''
    这道题有三种思路:
        1. 暴力法
        2. 双指针法(需要一个额外的m长度的数组)
        3. 倒序双指针法(不需要额外空间了)
'''
class Solution:
    def merge(self,nums1,m,nums2,n):
        end = m+n-1
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[end] = nums1[m-1]
                m -= 1
                end -= 1
            else:
                nums1[end] = nums2[n-1]
                n -= 1
                end -= 1
        if m:
            while m:
                nums1[end] = nums1[m-1]
                m -= 1
                end -= 1
        else:
            while n:
                nums1[end] =  nums2[n-1]
                n -= 1
                end -= 1

if __name__ == '__main__':
    s = Solution()
    nums1 = []
    nums2 = []
    m,n = 0,0
    s.merge(nums1,m,nums2,n)
    print(nums1)