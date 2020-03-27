class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        index = length = len(s)
        res = [s[0]]
        while index > 1:
            temp = set()
            for i in res:
                char = s[length - index + 1] # 待插入的字符
                for j in range(len(i)+1):
                    string = i[:j]+char+i[j:]
                    temp.add(string)
            res = list(temp)
            index -= 1
        return res  


class Solution:
    def permutation(self, s: str) -> List[str]:
        start = -1
        self.ans = []
        s1 = list(s)
        def dfs(start,s1):
            start += 1
            if start == len(s1)-1:
                self.ans.append(''.join(s1))
            for i in range(start,len(s)):
                s1[start],s1[i] = s1[i],s1[start]
                dfs(start,s1)
                s1[start],s1[i] = s1[i],s1[start]
        dfs(start,s1)
        c = []
        for i in set(self.ans):
            c.append(i)
        return c
                
