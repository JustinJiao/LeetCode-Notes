# LeetCode No.025 K个一组翻转链表
# 题目链接: https://leetcode.cn/problems/reverse-nodes-in-k-group/description/

#方法一：双指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        dummy = ListNode(0,head)
        prev = dummy
        while True:
            #确定这次的开头
            start = prev.next
            #看够不够k个
            kth = prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            #存储下一个
            next_group = kth.next
            kth.next = None
            #反转当前的
            new_head = reverse(start)
            
            #拼接一下
            prev.next = new_head
            prev = start
            prev.next = next_group
