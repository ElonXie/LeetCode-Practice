class Solution:
    def sumNums(self, n: int) -> int:
        return n and n+self.sumNums(n-1)


# 2. 快速乘
class Solution:
    def helper(self, A, B):
        ans = B and self.helper(A << 1, B >> 1)
        ans += B & 1 and A
        return ans

    def sumNums(self, n: int) -> int:
        return self.helper(n, n + 1) >> 1