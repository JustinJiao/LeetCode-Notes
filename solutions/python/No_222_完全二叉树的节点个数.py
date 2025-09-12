# LeetCode No.222 完全二叉树的节点个数
# 题目链接: https://leetcode.cn/problems/count-complete-tree-nodes/description/


from typing import List,Optional

#方法一：层级遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        result = 0
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                result +=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

#方法二：递归
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def help(cur):
            if not cur:
                return 0
            left = help(cur.left)
            right = help(cur.right)
            result = left + right +1
            return result
        return help(root)

#方法三：完全二叉树的性质
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 1
        left = root.left
        right = root.right
        while left and right:
            count +=1
            left = left.left
            right = right.right
        if not left and not right:
            return 2 ** count - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            
            
            
        
            
        