# LeetCode No.337 打家劫舍三
# 题目链接: https://leetcode.cn/problems/house-robber-iii/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def help(cur):
            if not cur:
                return [0,0]
            leftdp = help(cur.left)
            rightdp = help(cur.right)
            val0 = max(leftdp[0],leftdp[1])+max(rightdp[0],rightdp[1])#不偷
            val1 = cur.val + leftdp[0]+rightdp[0]#偷
            return [val0,val1]
        result = help(root)
        return max(result[0],result[1])