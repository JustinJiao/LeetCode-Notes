# LeetCode No.239 滑动窗口最大值
# 题目链接: https://leetcode.cn/problems/sliding-window-maximum/description/

#方法一：使用单调栈deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #这个function实现的是加入一个元素，并且把前面所有小于它的元素弹出
        def popfront(q,val):
            while q and val > q[-1]: 
                q.pop()
            q.append(val)
            
        from collections import deque
        result = []
        q = deque()

        for i in range(len(nums)):
            popfront(q,nums[i])
            if i >=k and nums[i-k] == q[0]:##i>-k意味着在前k个值的时候，不进行弹出操作
                q.popleft()                ## nums[i-k] == q[0]意味着，现在的最大值该弹出了，就不是最大值了
            if i >= k-1:                   ##意味着前k个元素的时候还没有形成滑动窗口，也就意味着不需要添加到result
                result.append(q[0])
        return result
            
            
            
        
            
        