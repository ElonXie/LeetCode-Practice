#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (59.05%)
# Likes:    448
# Dislikes: 0
# Total Accepted:    77.9K
# Total Submissions: 131.6K
# Testcase Example:  '3\n2'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 问总共有多少条不同的路径？
# 
# 
# 
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
# 
# 
# 
# 示例 1:
# 
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 
# 
# 示例 2:
# 
# 输入: m = 7, n = 3
# 输出: 28
# 
# 
# 
# 提示：
# 
# 
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10 ^ 9
# 
# 
#
import math
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ###方法1#############################################
        # 典型DP
        # ans = [ [0 for i in range(n)] for i in range(m)]
        # ans[0][0] = 1
        # for i in range(0,m):
        #     for j in range(0,n):
        #         if i+j==0: 
        #             continue
        #         else:
        #             if i==0:
        #                 ans[i][j] = ans[i][j-1]
        #             elif j==0:
        #                 ans[i][j] = ans[i-1][j]
        #             else:
        #                 ans[i][j] = ans[i-1][j]+ans[i][j-1]
        # return ans[m-1][n-1]


        ###方法2#############################################
        # size, loop = [m,n] if m<= n else [n,m]
        # ans = [1 for i in range(size)]
        # for i in range(loop-1):
        #     for j in range(size-2,-1,-1):
        #         ans[j] = ans[j]+ans[j+1]
        # return ans[0]


        #####方法3################################################
        return int(math.factorial(m+n-2)//math.factorial(m-1)//math.factorial(n-1))
                    

        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(57,2))
    print(math.factorial(57)//math.factorial(1)//math.factorial(56))