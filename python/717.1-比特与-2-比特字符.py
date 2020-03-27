#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#
# https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/description/
#
# algorithms
# Easy (47.03%)
# Likes:    113
# Dislikes: 0
# Total Accepted:    14.6K
# Total Submissions: 31K
# Testcase Example:  '[1,0,0]'
#
# 有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
# 
# 现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
# 
# 示例 1:
# 
# 
# 输入: 
# bits = [1, 0, 0]
# 输出: True
# 解释: 
# 唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# bits = [1, 1, 1, 0]
# 输出: False
# 解释: 
# 唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
# 
# 
# 注意:
# 
# 
# 1 <= len(bits) <= 1000.
# bits[i] 总是0 或 1.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # 这是正向递归呢还是反向呢? 像是正向回溯
        # 这个就模拟就行了.不用递归233
        # 也可以用DP. 从后向前扫. dp(i) = dp(i-1) if not i else dp(i-2) if i
        # def dfs(bits,L):
        #     if L == len(bits)-2 and bits[L]:
        #         return False
        #     if L == len(bits)-1 and not bits[L]:
        #         return True
        #     if not bits[L]:
        #         return dfs(bits,L+1)
        #     if bits[L]:
        #         return dfs(bits,L+2)
        # return dfs(bits,0)
        i = 0
        while i < len(bits):
            if i == len(bits)-1:
                return True
            if bits[i]:
                i+=2
            else:
                i += 1
        return False
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.isOneBitCharacter([1,0,0])
