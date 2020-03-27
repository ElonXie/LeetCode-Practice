#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (48.79%)
# Likes:    903
# Dislikes: 0
# Total Accepted:    59.6K
# Total Submissions: 121.6K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 从第一个柱子,向右找到任何一个最高的柱子.
        # 必须有局部极小值,才能存住水.
        # 从左至右看.假设 a[1] > a[2] > a[3] , a[4] > a[1]
        # 存水量为 1-2 + 2-3 + 1-4 + 2-4 + 3-4

        # 左右先找到两个局部极大. 计面积为 min(a1,a2) * (index2-index1-1)
        # a1继续增加. 面积减所有小于a1的值. 若遇a3>a1. 计新面积为

        # 假设a1<a2. 计算面积. 遇a3<a1则面积-a3. 遇a3>a1
                # 若 a3<a2 面积-a1+ (a3-a1)*(i3-i2)面积 并 L=a3
                # 若 a3>a2 面积-a1 + (a2-a1) * (i3-i2) 面积 并L = a3
        
        if not height:
            return 0
        # 新思路: 先找最大值. 再从整体删除.
        max_height = height[0]
        max_index_L = 0
        length = len(height)
        for i in range(length):
            if height[i] > max_height:
                max_index_L = i
                max_height = height[i]
        for i in range(length):
            if height[i] >= max_height:
                max_index_R = i
        L,R  = height[0],height[length-1]

        area = max_height*length
        for i in range(max_index_L):
            L = max(L,height[i])
            area = area - max_height + (L - height[i])
        for i in range(length-1,max_index_R,-1):
            R = max(R,height[i])
            area = area - max_height + (R - height[i])
        if max_index_R == max_index_L:
            return area - max_height
        else:
            for i in range(max_index_L+1,max_index_R):
                area = area -  height[i]
            return area - 2*max_height

# @lc code=end

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    s = Solution()
    s.trap(height)