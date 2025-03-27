# LeetCode No.202 快乐数
# 题目链接: https://leetcode.cn/problems/happy-number/description/


from typing import List

#方法一：集合
class Solution:
    def isHappy(self, n: int) -> bool:
        def getsum(n):
            new_num = 0
            while n:
                n,r = divmod(n,10)
                new_num += r **2
            return new_num
        record = set()
        while True:
            n = getsum(n)
            if n == 1:
                return True

            if n in record:
                return False
            else:
                record.add(n)
                
#方法二：双指针判断是否有无限循环    
class Solution:
    def isHappy(self, n: int) -> bool:
        def getsum(n):
            new_num = 0
            while n:
                n,r = divmod(n,10)
                new_num += r **2
            return new_num
        slow = n
        fast = n
        while getsum(fast)!=1 and getsum(getsum(fast)):
            slow = getsum(slow)
            fast = getsum(getsum(fast))
            if slow == fast:
                return False
        return True
            
            
            
            
        
            
        