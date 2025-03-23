#数组的插入和删除时间是O(n)因为数组在定义的时候，长度是固定的。
#如果想要更改数组的长度，就需要重新定义一个新的数组。

#链表的长度可以是不固定的，并且可以动态增删，适合数据量不固定，频繁增删，较少查询的场景

#定义一个链表结构
class ListNode:
    def __init__(self, val,next = None):
        self.val = val
        self.next = next