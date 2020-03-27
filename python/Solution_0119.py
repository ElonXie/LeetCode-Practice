# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:46:48 2020

@author: e
"""

'''
    思路:
        每一行是上一行的两个相邻数相加得到 --> 错位相加
        如 : [1,3,3,1] -> [1,4,6,4,1]
        可以看做: [1,3,3,1,0]
                 [0,1,3,3,1]
                 
     牛逼方法:
         第N行第j列 -- 组合数 C_n^j (时间复杂度为啥一样?因为乘法算起来就是多个加
                                      法?然后我们错位相加相当于用了乘法?)
'''

class Solution:
    def getRow(self,rowIndex):
#        ans = [1]
#        for j in range(1,rowIndex+1):
#            ans1 = ans + [0]
#            ans2 = [0] + ans
#            ans = [ans1[i]+ans2[i] for i in range(j+1)]
#        return ans
        ans = []
        res = 1
        ans.append(res)
        for j in range(1,rowIndex+1):
            res = int(res*(rowIndex+1-j)/j)
            ans.append(res)
        return ans
    
if __name__ == '__main__':
    s = Solution()
    ans = s.getRow(3)
    print(ans)