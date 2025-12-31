# LeetCode No.501 二叉搜索树中的众数
# 题目链接:https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/
from typing import Optional,List
# Definition for a binary tree node.
#方法一: 中序遍历+哈希表统计
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import Counter
        nums = []
        def help(cur):
            nonlocal nums
            if not cur:
                return None
            help(cur.left)
            nums.append(cur.val)
            help(cur.right)
        help(root)
        dic = Counter(nums)
        max_count = max(dic.values())
        result = []
        for val, freq in dic.items():
            if freq == max_count:
                result.append(val)
        return result
#方法二: 中序遍历+计数
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_count = 0
        cout = 0
        prev = None
        result = []
        def help(cur):
            nonlocal max_count,cout,prev,result
            if not cur:
                return None
            help(cur.left)

            if not prev:
                cout = 1
            elif cur.val == prev.val:
                cout +=1
            else:
                cout =1
            prev = cur

            if cout == max_count:
                result.append(cur.val)
            elif cout > max_count:
                max_count = cout
                result = [cur.val]

            help(cur.right)
        help(root)
        return result