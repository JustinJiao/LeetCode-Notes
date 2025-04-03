# LeetCode No.232 用栈实现队列
# 题目链接: https://leetcode.cn/problems/implement-queue-using-stacks/description/

import bisect
from typing import List

#方法一：两个栈维护
class MyQueue:

    def __init__(self):
        self.stack_int = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_int.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_int)):
                self.stack_out.append(self.stack_int.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return not (self.stack_int or self.stack_out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
            
            
            
        
            
        