# LeetCode No.515 在每个树行中找最大值
# 题目链接:https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
from typing import Optional,List
import sys
import ast

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
#方法一：
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        result = []
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            m = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                m = max(node.val,m)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(m)
        return result