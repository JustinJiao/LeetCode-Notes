# LeetCode No.21 合并两个有序链表
# 题目链接: https://leetcode.cn/problems/merge-two-sorted-lists/description/

#方法一：迭代
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur = ListNode(list1.val)
                list1 = list1.next
            else:
                cur = ListNode(list2.val)
                list2= list2.next
            prev.next = cur
            prev = cur
        if list1:
            prev.next = list1
        else:
            prev.next = list2
        return dummy.next
    
#方法二：递归
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            head = list1
            head.next = self.mergeTwoLists(list1.next,list2)
        else:
            head = list2
            head.next = self.mergeTwoLists(list1,list2.next)
        return head