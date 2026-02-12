# LeetCode No.230 二叉搜索树中第k小的元素
# 题目链接:https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/

#方法一：dfs后序遍历+最小堆
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        import heapq
        heap = []
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            dfs(cur.right)
            heapq.heappush(heap,-cur.val)
            if len(heap)>k:
                heapq.heappop(heap)
        dfs(root)
        return -heapq.heappop(heap)

#方法二：中序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = 0
        def dfs(cur):
            nonlocal k,result
            if not cur:
                return
            dfs(cur.left)
            k-=1
            if k == 0:
                result = cur.val
                return
            dfs(cur.right)
        dfs(root)
        return result

#方法三 ：栈模拟中序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k-=1
            if k == 0:
                return root.val
            root = root.right
