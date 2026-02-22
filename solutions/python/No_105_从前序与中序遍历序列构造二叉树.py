# LeetCode No.105 从前序与中序遍历序列构造二叉树
# 题目链接:https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {val:index for index,val in enumerate(inorder)}
        root_index = 0
        def help(left,right):
            nonlocal root_index
            if left > right:
                return None
            root_val = preorder[root_index]
            root_index+=1
            root = TreeNode(root_val)
            index = dic[root.val]
            root.left = help(left,index-1)
            root.right = help(index +1 ,right)
            return root
        return help(0,len(inorder)-1)