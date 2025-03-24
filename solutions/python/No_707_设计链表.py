# LeetCode No.707 设计链表
# 题目链接: https://leetcode.cn/problems/design-linked-list/

class ListNode:
    def __init__(self,val =0,next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummyHead = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummyHead.next
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        cur = ListNode(val,self.dummyHead.next)
        self.dummyHead.next = cur
        self.size+=1
    def addAtTail(self, val: int) -> None:
        cur = self.dummyHead
        while cur.next:
            cur = cur.next
        temp = ListNode(val)
        cur.next = temp
        self.size +=1
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        cur = self.dummyHead
        for i in range(index):
            cur = cur.next
        temp = ListNode(val,cur.next)
        cur.next = temp
        self.size+=1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.dummyHead
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -=1 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)