# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix: return []
#         L, R, T, B = 0, len(matrix[0])-1, 0, len(matrix)-1
#         res = []
#         while True:
#             for i in range(L,R+1):
#                 res.append(matrix[T][i])
#             T += 1
#             if T>B: break
#             for i in range(T,B+1):
#                 res.append(matrix[R][i])
#             R -= 1
#             if L>R: break
#             for i in range(R,L-1,-1):
#                 res.append(matrix[i][B+1])
#             B -= 1
#             if T>B: break
#             for i in range(B,T-1,-1):
#                 res.append(matrix[i][L])
#             L += 1
#             if L>R: break
#         return res
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        L,T,R,B = 0,0,len(matrix[0])-1,len(matrix)-1
        ans = []
        while (L<=R and T<=B):
            curRow = T
            curCol = L
            if L==R:
                while(curRow<=B):
                    ans.append(matrix[curRow][curCol])
                    curRow += 1
                break
            elif B==T:
                while(curRow<=R):
                    ans.append(matrix[curRow][curCol])
                    curCol += 1
                break
            while(curCol<R):
                ans.append(matrix[curRow][curCol])
                curCol += 1
            while(curRow<B):
                ans.append(matrix[curRow][curCol])
                curRow += 1
            while(curCol>L):
                ans.append(matrix[curRow][curCol])
                curCol -= 1
            while(curRow>T):
                ans.append(matrix[curRow][curCol])
                curRow -= 1
            L += 1
            T += 1
            B -= 1
            R -= 1
        return ans

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder(matrix))