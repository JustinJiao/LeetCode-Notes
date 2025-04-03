#栈
##方法一：用list实现
stack = []  # 创建一个空栈

stack.append(1)  # 压入元素
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

top_element = stack.pop()  # 弹出栈顶元素
print(top_element)  # 3
print(stack)  # [1, 2]

print(stack[-1])  # 访问栈顶元素，不删除它（2）

print(len(stack))  # 获取栈的大小（2）

##方法二用collections.deque
from collections import deque

stack = deque()  # 创建一个双端队列作为栈

stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # deque([1, 2, 3])

top_element = stack.pop()
print(top_element)  # 3
print(stack)  # deque([1, 2])

#队列
##方法一使用collections.deque
from collections import deque

queue = deque()  # 创建一个双端队列作为队列

queue.append(1)  # 入队
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

front_element = queue.popleft()  # 出队
print(front_element)  # 1
print(queue)  # deque([2, 3])

#方法二：使用queue.Queue
from queue import Queue

q = Queue()  # 创建队列（默认无限大小）

q.put(1)  # 入队
q.put(2)
q.put(3)

print(q.get())  # 出队，输出 1
print(q.get())  # 输出 2
print(q.get())  # 输出 3

print(q.empty())  # 是否为空，True

