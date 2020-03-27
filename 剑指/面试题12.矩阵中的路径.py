'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m,n = len(board),len(board[0])
        length = len(word)
        dir = [ [-1,0],[1,0],[0,-1],[0,1]  ]
        visited = [ [0]*n for _ in range(m)]
        def hasPath(i,j,cur_len):
            if board[i][j]== word[cur_len] and cur_len==length-1:
                return True
            visited[i][j] = 1
            for di,dj in dir:
                if i+di>-1 and i+di<m and j+dj>-1 and j+dj<n and visited[i+di][j+dj]==0 and board[i][j]==word[cur_len] and hasPath(i+di,j+dj,cur_len+1):
                    return True
            visited[i][j] = 0
            return False
        
        for i in range(m):
            for j in range(n):
                if hasPath(i,j,0):
                    return True
        return False
            





# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         self.length = len(word)
#         self.board = board
#         self.target = word
#         if not board or not board[0]:
#             return False
#         self.visited = [ [0 for i in range(len(board[0]))] for i in range(len(board)) ]
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 ans = self.hasPath(i,j,0)
#                 if ans:
#                     return True
#         return False

#     def hasPath(self,i,j,cur_len):
#         if cur_len==self.length:
#             return True
#         ans = False
#         if(i<len(self.board) and i>-1 and j<len(self.board[0]) and j>-1 and self.visited[i][j]==0 and self.board[i][j]==self.target[cur_len]):
#             self.visited[i][j] = 1
#             # ans_down = self.hasPath(i+1,j,cur_len+1)
#             # ans_on = self.hasPath(i-1,j,cur_len+1)
#             # ans_right = self.hasPath(i,j+1,cur_len+1) 
#             # ans_left = self.hasPath(i,j-1,cur_len+1)
#             # ans = ans_down or ans_on or ans_right or ans_left
#             ans = self.hasPath(i+1,j,cur_len+1) or self.hasPath(i-1,j,cur_len+1) or self.hasPath(i,j+1,cur_len+1) or self.hasPath(i,j-1,cur_len+1)
#             if not ans:
#                 self.visited[i][j] = 0
#         return ans
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board or not word: return False
#         m, n = len(board), len(board[0])
#         visit = [ [False] * n for _ in range(m)]
#         dirc = [(0,1), (1, 0), (0, -1), (-1, 0)]
#         def dfs(i, j, index):
#             if index == len(word): return True
#             visit[i][j] = True
#             for di, dj in dirc:
#                 ni, nj = i + di, j + dj
#                 if ni >= 0 and ni < m and nj >= 0 and nj < n and not visit[ni][nj] and board[ni][nj] == word[index] and dfs(ni, nj, index + 1):
#                     return True
#             visit[i][j] = False
#             return False



#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == word[0] and dfs(i, j, 1):
#                     return True
#         return False

if __name__ == '__main__':
    s = Solution()
    # board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
    # word = "aaaaa"
    # board=[["a","a"],["a","a"]]
    # word = "aaaaa"
    board = [["a"]]
    word = "a"
    print(s.exist(board,word))
    print('')