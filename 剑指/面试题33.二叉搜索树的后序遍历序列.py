from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        #二叉搜索树后续遍历的性质，最后一位是根节点，从前往后找到第一个比root大的节点，该节点分割左右子树 
        
        def dfs(tmp):
            if len(tmp) <=1:
                return True
            
            for i,c in enumerate(tmp):
                l = len(tmp)

                if c>=tmp[-1]:
                    for k in tmp[i:]:
                        if k < tmp[-1]:
                            return False
                    return dfs(tmp[:i]) and dfs(tmp[i:l-1])

            return True
        
        return dfs(postorder)



class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 第一个大于root的是右root,第一个小于root的是左root,递归

        def search(L,R):
            if L==R:
                return True
            large,small = -1,-1
            leftNode,rightNode = L-1,L-1
            leftLarge = L-1
            for i in range(R-1,L-1,-1):
                if postorder[i]>=postorder[R]:
                    if large==-1:
                        large = 1
                        rightNode = i
                    leftLarge = i
                if small==-1 and postorder[i]<postorder[R]:
                    small = 1
                    leftNode = i
            if leftNode==L-1:
                return search(L,rightNode)
            elif rightNode==L-1:
                return search(L,leftNode)
            else:
                if leftNode>= rightNode:
                    return False
                if leftLarge!=L-1 and leftLarge<leftNode:
                    return False
                else:
                    return search(L,leftNode) and search(leftNode+1,rightNode)
        return search(0,len(postorder)-1)

if __name__ == '__main__':
    s = Solution()
    print(s.verifyPostorder([7, 4, 6, 5]))


                    

