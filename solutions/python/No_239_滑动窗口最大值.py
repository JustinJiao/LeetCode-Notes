# LeetCode No.239 滑动窗口最大值
# 题目链接: https://leetcode.cn/problems/sliding-window-maximum/description/

#方法一：使用单调栈deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque()
        result = []
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:#维护单调递减的队列
                queue.pop()
            queue.append(i)
            if queue and queue[0] <= i-k:#如果队列头部的元素已经不在窗口中了，那么就把它弹出
                queue.popleft()
            if i >= k-1:
                result.append(nums[queue[0]])
        return result