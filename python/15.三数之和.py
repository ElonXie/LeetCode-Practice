#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (25.67%)
# Likes:    1868
# Dislikes: 0
# Total Accepted:    168.4K
# Total Submissions: 652.4K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            L, R = i+1, len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            while L<R:
                sum = nums[i]+nums[L]+nums[R]
                if sum<0:
                    L += 1
                elif sum>0:
                    R -= 1
                else:
                    ans.append([nums[i],nums[L],nums[R]])
                    while L<R and nums[L+1]==nums[L]:
                        L+=1
                    while L<R and nums[R-1] == nums[R]:
                        R -= 1
                    L += 1
                    R -= 1
        return ans


# @lc code=end
def rightAns(nums):
    nums.sort()
    dict = {}
    ans = []
    length = len(nums)
    for i in range(length-2):
        for j in range(i+1,length-1):
            for k in range(j+1,length):
                if nums[i]+nums[j]+nums[k] == 0:
                    ans1 = str(nums[i])+str(nums[j])+str(nums[k])
                    if ans1 not in dict:
                        dict[ans1] = 1
                        ans.append([nums[i],nums[j],nums[k]])
    return ans

import random
def generate_right_nums(size,value):
    arr_size = random.randint(0,size+1)
    arr = [ int(random.random()*(value+1)-random.random()*value) for i in range(arr_size)]
    return arr

if __name__ == "__main__":
    s = Solution()
    ans = True
    for i in range(100):
        arr = generate_right_nums(15,5)
        if s.threeSum(arr) != rightAns(arr):
            ans = False
            print(s.threeSum(arr))
            print(rightAns(arr))
            print('current loop : {}'.format(i))
            break
    print('your ans is : {}'.format(ans))
        

