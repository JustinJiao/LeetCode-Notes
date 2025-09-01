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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        resulst = []
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            resulst.append(node.val)
        return resulst