# LeetCode No.23 合并k个升序链表
# 题目链接: https://leetcode.cn/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
        if not lists:
            return None
        result = lists[0]
        for i in range(1,len(lists)):
            result = merge(result,lists[i])
        return result
                    
        def divid(left,right):
            if left == right:
                return lists[left]
            mid = (left + right) //2
            l1 = divid(left,mid)
            l2 = divid(mid+1,right)
            return merge(l1,l2)
        return divid(0,len(lists)-1)
