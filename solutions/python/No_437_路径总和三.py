# LeetCode No.437 路径总和 III
# 题目链接: https://leetcode.cn/problems/path-sum-iii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict
        prefix = defaultdict(int)
        prefix[0] +=1
        def help(cur,cursum):
            if not cur:
                return 0
            cursum += cur.val
            count = prefix[cursum-targetSum]
            prefix[cursum] +=1
            left = help(cur.left,cursum)
            right = help(cur.right,cursum)
            prefix[cursum] -=1
            return count+left+right
        return help(root,0)

        
        
            
        