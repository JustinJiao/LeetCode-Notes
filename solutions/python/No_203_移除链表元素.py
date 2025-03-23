# LeetCode No.203 移除链表元素
# 题目链接: https://leetcode.cn/problems/remove-linked-list-elements/description/


#方法一：
# Definition for singly-linked list.
from typing import List
import sys
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(next = head)
    cur = dummy
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next

def build_link_list(l:List[int])-> ListNode:
    dummy = ListNode(0)
    cur = dummy
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    return dummy.next

def linkListToList(head:ListNode)->List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    l = list(map(int,data[1:n+1]))
    val = int(data[n+1])
    
    head = build_link_list(l)
    result = removeElements(head,val)
    print("".join(map(str,linkListToList(result))))

if __name__ == "__main__":
    main()
    
    
            
            
        
            
        