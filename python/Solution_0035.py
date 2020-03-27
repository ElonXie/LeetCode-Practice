# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:39:23 2020

@author: e
"""


'''
    二分查找
'''

class Solution:
    def searchInsert(self,nums,target):
        #一个典型的二分查找.但是被查找数可能不在nums中,需要返回被插入的位置,即nums[index]>target,nums[index-1]<target
        low,high = 0,len(nums)-1
        index = low if nums[low]>=target else (high+1 if nums[high]<target else (high if nums[high]==target else -1))
        #上边这一句可以去掉 不等式里的等号
        if index>-1:
            return index
        #mid = low+(high-low)//2 #如果长度为2,mid=0 也就是会出现mid = low+(high-low)//2  mid==low作为终止条件
        while 1:
            mid = low+(high-low)//2 
            if mid == low:
                index = low if nums[low]==target else high
                return index
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                low = mid
            else:
                high = mid
        
        
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    ans = s.searchInsert(nums,4)
    print(ans)