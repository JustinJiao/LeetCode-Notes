# LeetCode No.968 监控二叉树
# 题目链接: https://leetcode.cn/problems/binary-tree-cameras/description/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #状态转移，利用后序遍历，看左右孩子的状态，决定当前节点的状态
        #状态共分3种：0：无覆盖 1:放置摄像头 2:有覆盖
        #情况有四种：
        #1:如果左右孩子均为有覆盖2，那么当前节点为0，无覆盖
        #2：如果左右孩子有一个为0，那么当前节点为1，放置一个摄像头
        #3:如果左右孩子有一个为1，那么当前节点为有覆盖2
        #4:如果最后根节点还是为0，那么需要多加入一个摄像头覆盖根节点
        #注意：在遇到NULL的时候要判断为2，因为在寻找最少放置
        result = 0
        def help(cur):
            nonlocal result
            if not cur:
                return 2
            left = help(cur.left)
            right = help(cur.right)
            if left == 2 and right ==2: #1
                return 0
            if left == 0 or right == 0: #2
                result +=1
                return 1
            if left == 1 or right ==1: #3
                return 2
        if help(root) == 0:
            result +=1
        return result

