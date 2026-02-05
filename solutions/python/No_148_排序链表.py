# LeetCode No.148 排序链表
# 题目链接:https://leetcode.cn/problems/sort-list/description/

#方法一：直接排序
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        l.sort()
        cur = head
        for val in l:
            cur.val = val
            cur = cur.next
        return head

#方法二：归并排序
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1,l2):
            dummy = ListNode(0)
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 if l1 else l2
            return dummy.next
        def help(node):
            if not node or not node.next:
                return node
            slow,fast = node,node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow
            left_half = node
            right_half = mid.next
            mid.next = None
            left = help(left_half)
            right = help(right_half)
            return merge(left,right)

        return help(head)

