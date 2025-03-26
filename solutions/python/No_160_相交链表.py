# LeetCode No.160 相交链表
# 题目链接: https://leetcode.cn/problems/intersection-of-two-linked-lists/

#方法一：双指针
from typing import Optional
import sys
import ast

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
#方法一：双指针+尾部对齐
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = 0
        l2 = 0
        cur1 = headA
        cur2 = headB
        while cur1:
            cur1 = cur1.next
            l1 += 1
        while cur2:
            cur2 = cur2.next
            l2 += 1
        h1 = headA
        h2 = headB
        n = abs(l1 -l2)
        listNum = 0

        if l1 > l2:
            listNum = 1
        else:
            ListNum = 2

        if listNum == 1:
            for i in range(n):
                h1 = h1.next
        else:
            for i in range(n):
                h2 = h2.next

        while h1 and h2:
            if h1 == h2:
                return h1
            else:
                h1 = h1.next
                h2 = h2.next
        return None

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
    
    
            
            
        
            
        