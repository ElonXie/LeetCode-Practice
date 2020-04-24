#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.29%)
# Likes:    331
# Dislikes: 0
# Total Accepted:    40.6K
# Total Submissions: 174.2K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp
        if not s:
            return 0
        if s[0] == '0':
            return 0
        if len(s)==1:
            return 1
        if s[-2:]=='00':
            return 0
        dp = [0] * len(s)
        def parseWrod(word):
            num = int(word)
            if num==0:
                return 0
            if num>26:
                if word[1]=='0':
                    return 0
                return 1
            if word[0] == '0':
                return 4
            if word[1] == '0':
                return 2
            return 3           

        word_type = parseWrod(s[-2:])
        if word_type==0:
            return 0
        if word_type==1:
            dp[-1] = 1
            dp[-2] = 1
        elif word_type==2:
            dp[-1] = 0
            dp[-2] = 1
        elif word_type==3:
            dp[-1] = 1
            dp[-2] = 2
        else:
            dp[-1] = 1
            dp[-2] = 0
        # 连续两个数字 有可能三种情况:
        # 1 : 仅单个有效.  2 : 必须连着两个  3 : 即可一个,又可两个 4.当前数字无效
        for i in range(len(s)-3,-1,-1):
            word_type = parseWrod(s[i:i+2])
            if word_type==0:
                return 0
            if word_type == 1:
                dp[i] = dp[i+1]
            elif word_type == 2:
                dp[i] = dp[i+2]
            elif word_type == 3:
                dp[i] = dp[i+1]+dp[i+2]
            else:
                dp[i] = 0
        return dp[0]
# @lc code=end

