#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
# https://leetcode-cn.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (31.47%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 62.5K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 
# 给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n
# 朵花？能则返回True，不能则返回False。
# 
# 示例 1:
# 
# 
# 输入: flowerbed = [1,0,0,0,1], n = 1
# 输出: True
# 
# 
# 示例 2:
# 
# 
# 输入: flowerbed = [1,0,0,0,1], n = 2
# 输出: False
# 
# 
# 注意:
# 
# 
# 数组内已种好的花不会违反种植规则。
# 输入的数组长度范围为 [1, 20000]。
# n 是非负整数，且不会超过输入数组的大小。
# 
# 
# 
from typing import List
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 遍历花坛,两花间隔//2,即为两花间可插入数量
        # 两边分别以-1 和 len(flowerbed)为起始
        start,end = -2,len(flowerbed)+1
        res = 0
        
        for i in range(end-1):
            if flowerbed[i]:
                res += (i-start-2)//2
                start = i
                
        if res>=n:
            return True
        if start==-2:
            res = (end-start-2)//2
            return res>=n
        for i in range(end-2,-1,-1):
            if flowerbed[i]:
                res += (end-i-2)//2
                break
        return res>=n
            
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    arr = [0,0,]
    n = 2
    print(s.canPlaceFlowers(arr,n))