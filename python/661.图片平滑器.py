#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
# https:////leetcode-cn.com//problems//image-smoother//description//
#
# algorithms
# Easy (52.84%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 12.8K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入)
# ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
# 
# 示例 1:
# 
# 
# 输入:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# 输出:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3//4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5//6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8//9) = 平均(0.88888889) = 0
# 
# 
# 注意:
# 
# 
# 给定矩阵中的整数范围为 [0, 255]。
# 矩阵的长和宽的范围均为 [1, 150]。
# 
# 
#

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rows, cols = len(M),len(M[0])
        def calc_avg(M,X,Y):
            if len(M)==1:
                if len(M[0])==1:
                    return M[0][0]
                else:
                    if Y==0:
                        return (M[0][0]+M[0][1])//2
                    if Y==len(M[0])-1:
                        return (M[0][-1]+M[0][-2])//2
                    else:
                        return (M[0][Y]+M[0][Y-1]+M[0][Y+1])//3
            if len(M[0])==1:
                if X==0:
                    return (M[0][0]+M[1][0])//2
                if X==len(M)-1:
                    return (M[-1][0]+M[-2][0])//2
                else:
                    return (M[X][0]+M[X-1][0]+M[X+1][0])//3
            if X==0:
                if Y==0:
                    return (M[0][0]+M[1][0]+M[0][1]+M[1][1])//4
                elif Y==len(M[0])-1:
                    return (M[0][-1]+M[1][-1]+M[0][-2]+M[1][-2])//4
                else:
                    return (M[0][Y]+M[0][Y-1]+M[0][Y+1]+M[1][Y]+M[1][Y+1]+M[1][Y-1])//6
            elif X==len(M)-1:
                if Y==0:
                    return (M[-1][0]+M[-1][1]+M[-2][0]+M[-2][1])//4
                elif Y==len(M[0])-1:
                    return (M[-1][-1]+M[-1][-2]+M[-2][-1]+M[-2][-2])//4
                else:
                    return (M[-1][Y]+M[-1][Y-1]+M[-1][Y+1]+M[-2][Y]+M[-2][Y+1]+M[-2][Y-1])//6
            else:
                if Y==0:
                    return (M[X][Y]+M[X-1][Y]+M[X+1][Y]+M[X][Y+1]+M[X-1][Y+1]+M[X+1][Y+1])//6                    
                elif Y==len(M[0])-1:
                    return (M[X][Y]+M[X-1][Y]+M[X+1][Y]+M[X][Y-1]+M[X-1][Y-1]+M[X+1][Y-1])//6                    
                else:
                    return (M[X-1][Y-1]+M[X-1][Y]+M[X-1][Y+1]+M[X][Y-1]+M[X][Y]+M[X][Y+1]+M[X+1][Y-1]+M[X+1][Y]+M[X+1][Y+1])//9
        res = []
        for i in range(rows):
            res.append([])
            for j in range(cols):
                res[-1].append(calc_avg(M,i,j))
        return res
# @lc code=end

