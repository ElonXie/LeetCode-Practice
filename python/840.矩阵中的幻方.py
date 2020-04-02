#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#
# https://leetcode-cn.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Easy (33.69%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 14.6K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# 3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
# 
# 给定一个由整数组成的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
# 
# 
# 
# 示例：
# 
# 输入: [[4,3,8,4],
# ⁠     [9,5,1,9],
# ⁠     [2,7,6,2]]
# 输出: 1
# 解释: 
# 下面的子矩阵是一个 3 x 3 的幻方：
# 438
# 951
# 276
# 
# 而这一个不是：
# 384
# 519
# 762
# 
# 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
# 
# 
# 提示:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # 先找5. 以5为中心的,判断它是不是
        if len(grid)<3 or len(grid)<3:
            return 0
        ans = 0
        def sumRow(grid,i,j):
            return 15==(grid[i][j-1]+grid[i][j]+grid[i][j+1])
        def sumCol(grid,i,j):
            return 15==(grid[i-1][j]+grid[i][j]+grid[i+1][j])
        def sumDuiJiao(grid,i,j):
            sum1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
            sum2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
            return (15==sum1) and (15==sum2)
        def notSame(grid,i,j):
            bucket = [0] * 9
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if grid[x][y]<10 and grid[x][y]>0:
                        bucket[grid[x][y]-1]+=1
                        if bucket[grid[x][y]-1]==2:
                            return False
                    else:
                        return False
            return True
        def isHuanFang(grid,i,j):
            res = notSame(grid,i,j)
            if not res:
                return res
            for x in range(i-1,i+2):
                res = sumRow(grid,x,j)
                if not res:
                    return res
            for y in range(j-1,j+2):
                res = sumCol(grid,i,y)
                if not res:
                    return res
            return sumDuiJiao
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j]==5 and isHuanFang(grid,i,j):
                    ans += 1
        return ans
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.numMagicSquaresInside([[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]])