'''
    这题很傻逼,有None被压入栈,还要整最小值.所以不要维护最小值,还是用栈顶元素作判断吧
'''


'''定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次
 '''
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.main_stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        elif self.min_stack[-1] > x:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])



    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.main_stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()