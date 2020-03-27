# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:15:26 2020

@author: e
"""

class Solution:
    def removeElement(self,nums,val):
        if not nums:
            return
        i,j = 0,len(nums)-1
        while i<j:
            if nums[i]==val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        if nums[i] == val:
            return i
        return i+1
            
            
if __name__=='__main__':
    s = Solution()
    nums1 = [3,2,2,3]
    val1 = 3
    len1 = s.removeElement(nums1,val1)
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    len2 = s.removeElement(nums2,val2)
    print(len1,':',nums1[:len1])
    print(len2,':',nums2[:len2])