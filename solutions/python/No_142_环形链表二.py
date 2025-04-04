# LeetCode No.142 环形链表二
# 题目链接: https://leetcode.cn/problems/linked-list-cycle-ii/

from typing import Optional
import sys
import ast

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
#方法一：双指针
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                index1 = fast
                index2 = head
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
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
    

if __name__ == "__main__":
    main()
    
    
            
            
        
            
        