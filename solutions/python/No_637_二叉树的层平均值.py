# LeetCode No.199 二叉树的右视图
# 题目链接:https://leetcode.cn/problems/binary-tree-right-side-view/description/
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        result = []
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            sum = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sum/size)
        return result