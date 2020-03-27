#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (64.74%)
# Likes:    398
# Dislikes: 0
# Total Accepted:    63.9K
# Total Submissions: 98.6K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # DP
        rows,cols = len(grid),len(grid[0])
        valGrid = [[0]*cols] * rows
        # valGrid[rows-1][cols-1] = grid[rows-1][cols-1]
        # 任意一个点. 三种情况
            # 只有下.
            # 只有右
            # 下右都有
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if i==rows-1:
                    if j==cols-1:
                        continue
                    valGrid[i][j] = valGrid[i][j+1]+grid[i][j+1]
                elif j == cols-1:
                    valGrid[i][j] = valGrid[i+1][j] + grid[i+1][j]
                else:
                    valGrid[i][j] =min(valGrid[i][j+1]+grid[i][j+1],valGrid[i+1][j] + grid[i+1][j])
        return valGrid[0][0]+grid[0][0]
    
                    
                    
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,3,1],[1,5,1],[4,2,1]]
    s.minPathSum(matrix)