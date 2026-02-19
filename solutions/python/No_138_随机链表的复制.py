# LeetCode No.138 随机链表的复制
# 题目链接: https://leetcode.cn/problems/copy-list-with-random-pointer/description/

#方法一：字典存储
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                dic[cur].next = dic[cur.next]
            if cur.random:
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]
#方法二：原地复制
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        cur = head
        while cur:
            new_node = Node(cur.val)
            next_ = cur.next
            cur.next = new_node
            new_node.next = next_
            cur = next_
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        new_head = cur.next
        while cur:
            new_node = cur.next
            cur.next = new_node.next
            if cur.next:
                new_node.next = cur.next.next
            cur = cur.next
        return new_head