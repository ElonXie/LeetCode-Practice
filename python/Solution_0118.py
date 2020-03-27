# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:21:17 2020

@author: e
"""

'''
    杨辉三角问题 -- 这个问题我不熟悉
    思路:
        1. 首先想到的是模拟法,但是肯定效率低.因为需要遍历上一层list
            杨辉三角有对称性(但是没必要考虑这个对称性,节省不了多少时间.)
'''

class Solution:
    def generate(self,numRows):
        ans = [ [1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                if j<=i//2:
                    ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
                else:
                    ans[i][j] = ans[i][i-j]
        return ans
    
if __name__=='__main__':
    s = Solution()
    ans = s.generate(6)
    print(ans)
                    