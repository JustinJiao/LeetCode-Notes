# LeetCode No.206 翻转链表
# 题目链接: https://leetcode.cn/problems/reverse-linked-list/description/

#方法一：双指针
from typing import Optional
import sys
import ast

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
#方法一：双指针        
""" def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    pre = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre """
#方法二：递归
def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    def resverse(cur,pre):
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return resverse(temp,cur)
    return resverse(head,None)

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
    data = ast.literal_eval(sys.stdin.readline().strip())
    linklist = list_To_Linklist(data)
    result = reverseList2(linklist)
    result2 = linklist_to_list(result)
    print(result2)

if __name__ == "__main__":
    main()
    
    
            
            
        
            
        