#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.08%)
# Likes:    1950
# Dislikes: 0
# Total Accepted:    222.4K
# Total Submissions: 762.2K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ''
#         # 是他妈很难嗷
#         # 1. dp
#         dp = [[False]*len(s) for i in range(len(s))]
#         dp[-1][-1] = True
#         for i in range(len(s)-2,-1,-1):
#             dp[i][i] = True
#             dp[i][i+1] = s[i+1]==s[i]
#             for j in range(i+2,len(s)):
#                 dp[i][j] = (dp[i+1][j-1] and s[j]==s[i])
#         max_length = -1
#         for i in range(len(s)-1,-1,-1):
#             for j in range(i,len(s)):
#                 if dp[i][j]:
#                     max_index = j
#             if max_length<(max_index-i+1):
#                 max_length = max_index-i+1
#                 ans = s[i:max_index+1]
#         return ans
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        # 2. 简化空间
        max_length = 1
        ans = s[-1]
        # max_index = -1
        dp = [False] * len(s)
        dp[-1] = True
        for i in range(len(s)-2,-1,-1):
            # dp[i] = True
            max_cur = 0
            max_index = i
            for j in range(len(s)-1,i+1,-1):
                dp[j] = dp[j-1] and (s[i]==s[j])
                if dp[j] and (j-i+1>max_cur):
                    max_cur = j-i+1
                    max_index = j
            if s[i] == s[i+1]:
                dp[i+1] = True
                if max_cur<2:
                    # max_index = i+1
                    max_cur = 2
                    max_index = i+1
            else:
                dp[i+1] = False
            dp[i] = True
            if max_cur>max_length:
                ans = s[i:max_index+1]
                max_length = max_cur
        return ans
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome("abacab")