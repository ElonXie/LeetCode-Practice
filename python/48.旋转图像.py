#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
# https://leetcode-cn.com/problems/rotate-image/description/
#
# algorithms
# Medium (67.02%)
# Likes:    373
# Dislikes: 0
# Total Accepted:    56.9K
# Total Submissions: 84.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定 matrix =
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
#
#
# 示例 2:
#
# 给定 matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
#
#
#

# @lc code=start

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # i从0-j,代表当前行的第i个元素. 内循环j不动.代表当前右界
        i,j = 0,len(matrix[0])-1
        while i<j:
            cur = 0
            while cur<j-i:
                matrix[i][i+cur],matrix[cur+i][j],matrix[j][j-cur],matrix[j-cur][i]=   \
                    matrix[j-cur][i],matrix[i][i+cur],matrix[cur+i][j],matrix[j][j-cur]
                cur+=1
            i+=1
            j-=1
        return matrix
# @lc code=end

if __name__=='__main__':
    matrix = [ [i+5*j+1 for i in range(5)] for j in range(5) ]
    for num in matrix:
        print(num)
    s = Solution()
    matrix = s.rotate(matrix)
    for num in matrix:
        print(num)

