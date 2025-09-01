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
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        result = []
        queue = deque()
        if root:
            queue.append(root)
        else:
            return []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(level)
        return result
