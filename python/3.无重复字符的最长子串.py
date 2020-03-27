#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 感觉可以动态规划 --> 不是动态规划,是滑动窗口
        '''
            思路:
                用一个哈希表存每个字符的最新数值
                用一个慢指针指向当前字符串的首位
                慢指针指向字符串下一个位
                如果新字符在哈希表查找到的value在慢指针后边.
                    length更新,慢指针更新
                如果新字符在哈希表的value在慢指针之前,length+1,快指针加一
        '''
        i = 0
        length = 0
        max_len = 0
        dic = {}
        for index,c in enumerate(s):
            if c not in dic:
                dic[c] = index
                length += 1
            else:
                max_len = max(length,max_len)
                if dic[c]<i:
                    length += 1
                else:
                    i = dic[c]+1                    
                    length = index-i+1
                dic[c] = index              
            #print('step:{},max_len:{}'.format(index,max_len))
        max_len = max(length,max_len)
        return max_len

        ## 注: 本题解中采用的方法较优,但稍微复杂.略微简单些的思路是
        #   双指针一次仅滑动一个,且只滑动1,dic维护快慢指针之间的char
        #   当慢指针更新时,dic中要remove掉原指针指向的元素
        
if __name__ == '__main__':
    s = Solution()
    str1 = 'abcabcbb'
    print('length',s.lengthOfLongestSubstring(str1))
        
# @lc code=end

