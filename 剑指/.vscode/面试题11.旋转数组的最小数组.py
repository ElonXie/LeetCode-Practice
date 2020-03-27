'''把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
'''
from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        self.nums = numbers
        L,R = 0,len(numbers)-1
        while L < R:
            Mid = L+(R-L)//2
            if numbers[Mid]==numbers[L] and numbers[Mid]==numbers[R]:
                return self.find()
            if numbers[Mid]<=numbers[R]:
                R = Mid
                continue
            if numbers[Mid]>=numbers[L]:
                L = Mid+1
                continue
            
        return numbers[R]
    def find(self):
        for index in range(len(self.nums)-1):
            if self.nums[index+1]<self.nums[index]:
                return self.nums[index+1]
        return self.nums[0]
if __name__ == '__main__':
    s = Solution()
    nums1= [3,4,5,1,2]
    nums2 = [2,2,2,0,1]
    nums3 = [1,1,1,0,1]
    nums4 = [1,0,1,1,1]
    nums5 = [1,1,1,1,1]
    print(s.minArray(nums5))