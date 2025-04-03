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


#堆
#heapq 是 默认最小堆，也就是最小的元素在开头。

#创建最小堆
import heapq

heap = []  # 定义一个空堆
heapq.heappush(heap, 3)  # 插入元素 3 O(logn)
heapq.heappush(heap, 1)  # 插入元素 1
heapq.heappush(heap, 5)  # 插入元素 5

print(heap)  # 输出 [1, 3, 5]，堆的最小值在索引 0 处

#取值：
min_val = heapq.heappop(heap)  # 弹出堆顶（最小值）
print(min_val)  # 输出 1
print(heap)  # [3, 5]
#heapq.heapop()删除并返回堆顶元素 O(log n)

min_val = heap[0]  # 直接访问堆顶元素（最小值） O(1)
print(min_val)  # 输出 3 


#一次性建立最小堆
nums = [3, 1, 5, 2, 4]
heapq.heapify(nums)  # 直接转换为最小堆
print(nums)  # 输出 [1, 2, 5, 3, 4]，最小值在索引 0


#实现最大堆
max_heap = []
heapq.heappush(max_heap, -3)  # 插入 -3
heapq.heappush(max_heap, -1)  # 插入 -1
heapq.heappush(max_heap, -5)  # 插入 -5

print(-heapq.heappop(max_heap))  # 输出 5（最大值）
#插入-x,取出用-heapq.heappop(max_heap)即可


#获取前k个最小的元素
nums = [5, 2, 9, 1, 7, 6]
print(heapq.nsmallest(3, nums))  # 输出 [1, 2, 5]
O(nlogk)

#获取前k个最大的元素
print(heapq.nlargest(3, nums))  # 输出 [9, 7, 6]

