# LeetCode No.019 删除链表的倒数第N个节点
# 题目链接: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/

#方法一：双指针
from typing import Optional
import sys
import ast

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
#方法一：虚拟头节点+双指针   
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = dummy
        for _ in range(n+1):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

def list_To_Linklist(list):
    if len(list) == 0:
        return None
    dummy = ListNode(0)
    cur = dummy
    for val in list:
        temp = ListNode(val)
        cur.next = temp
        cur = cur.next
    return dummy.next
        
def linklist_to_list(head):
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    l = list(map(int,data[1:]))
    linklist = list_To_Linklist(l)
    result = removeNthFromEnd(linklist,n)
    result2 = linklist_to_list(result)
    print(result2)

if __name__ == "__main__":
    main()
    
##方法二：计算长度
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur:
            size+=1
            cur = cur.next
        dummy = ListNode(next = head)
        cur = dummy
        for i in range(size-n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
    
    
            
            
        
            
        