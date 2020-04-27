#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (41.21%)
# Likes:    1542
# Dislikes: 0
# Total Accepted:    262.9K
# Total Submissions: 634.5K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        def match(s1,s2):
            if s1==')' and s2=='(': return True
            if s1==']' and s2=='[': return True
            if s1=='}' and s2=='{': return True
            return False
        left,right = ['(','[','{'] , [')',']','}']
        stack = []
        for s1 in s:
            if s1 in left:
                stack.append(s1)
            else:
                if not stack:
                    return False
                s2 = stack.pop()
                if not match(s1,s2):
                    return False
        if len(stack)>0:
            return False
        return True
              
        
# @lc code=end
