# LeetCode No.234 回文链表
# 题目链接: https://leetcode.cn/problems/palindrome-linked-list/

import bisect
from typing import List

#方法一：快慢指针+反转链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        left = head
        right = prev
        while right:
            if left.val!= right.val:
                return False
            right = right.next
            left = left.next
        return True

#方法二：数组

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        return l == l[::-1]