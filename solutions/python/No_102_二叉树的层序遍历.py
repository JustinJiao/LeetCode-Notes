# LeetCode No.102 二叉树的层序遍历
# 题目链接:https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        result = []
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            l = []
            for _ in range(len(queue)):
                node = queue.popleft()
                l.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(l)
        return result
    
#方法二：DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node,depth):
            if not node:
                return
            
            if len(result) == depth:
                result.append(node.val)
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        dfs(root,0)
        return result