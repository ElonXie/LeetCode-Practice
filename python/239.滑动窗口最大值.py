#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (44.79%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    41.5K
# Total Submissions: 89.6K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 
# 返回滑动窗口中的最大值。
# 
# 
# 
# 进阶：
# 
# 你能在线性时间复杂度内解决此题吗？
# 
# 
# 
# 示例:
# 
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
# ⁠ 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = []
        for i in range(k):
            while len(queue)>0 and nums[queue[-1]]<=nums[i]:
                queue.pop(-1)
            queue.append(i)
        ans.append(nums[queue[0]])
        for i in range(k,len(nums)):
            if queue[0]<=i-k:
                queue.pop(0)
            while len(queue)>0 and nums[queue[-1]]<=nums[i]:
                queue.pop()
            queue.append(i)
            ans.append(nums[queue[0]])
        return ans
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)

