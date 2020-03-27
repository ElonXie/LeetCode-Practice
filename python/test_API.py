class Solution:
    def get(self,nums,k):
        dic = dict()
        for index,num in enumerate(nums):
            print(index,num)
            if num in dic:

                print(dic[num])
            if num not in dic:
                print('bucunzai')
                dic[num] = index
            else:
                print('cunzai')
                if index-dic[num]>k:
                    dic[num] = index
                else:
                    return True
        return False
        
if __name__ =='__main__':
    s = Solution()
    nums = [1,0,1,1]
    k = 1
    print(s.get(nums,k))
    
