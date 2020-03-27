# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:29:30 2020

@author: e
"""

'''
    思路:
        1. 倒序遍历到非9时,就可以+1 return了
        2. 提出整个数组,+1后,再转换成数组(用到了str)
        注:常用的拼接整数成长整数的思路就是str
'''


#class Solution:
#    def plusOne(self,digits):
#        d = 1
#        for i in range(len(digits)-1,-1,-1):
#            new_digit = digits[i]+d
#            digits[i] = new_digit%10
#            d = new_digit//10
#            if not d:
#                return digits
#        if not digits[0]+digits[-1]:
#            digits[0] = 1
#            digits.append(0)
#        return digits
#    
    
class Solution:
    def plusOne(self, digits):
        s = [str(i) for i in digits]
        return [int(i) for i in list(str(int(''.join(s)) + 1))]
    
if __name__=='__main__':
    a = Solution()
    nums = [9]
    ans = a.plusOne(nums)
    print(ans)