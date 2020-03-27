'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 1：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
'''

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [ [False]*n for _ in range(m)]
        # dirs = [ [0,1],[0,-1],[1,0],[-1,0] ]
        dirs = [[0,1],[1,0]]
        def sums(i,j):
            sum = 0
            while(i>0):
                sum += i%10
                i = i//10
            while(j>0):
                sum += j%10
                j = j//10
            return sum
        def countPathes(i,j): 
            count = 0
            visited[i][j] = True
            for di,dj in dirs:
                if i+di<m and i+di>-1 and j+dj<n and j+dj>-1 and not visited[i+di][j+dj] and sums(i+di,j+dj)<=k:
                    count_sub = countPathes(i+di,j+dj)
                    count += count_sub
            return count+1
        return countPathes(0,0)

if __name__ == '__main__':
    s = Solution()
    ans = s.movingCount(3,3,2)
    print(ans)

