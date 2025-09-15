# LeetCode No.257 二叉树的所有路径
# 题目链接: https://leetcode.cn/problems/binary-tree-paths/description/
from typing import List,Optional

#方法一：递归
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def help(cur,path,result):
            path.append(cur.val)
            if not cur.left and not cur.right:
                rPath = '->'.join(map(str,path))
                result.append(rPath)
                return
            if cur.left:
                help(cur.left,path,result)
                path.pop()
            if cur.right:
                help(cur.right,path,result)
                path.pop()

        path = []
        result = []
        if not root:
            return result
        help(root,path,result)
        return result
            
        
            
        