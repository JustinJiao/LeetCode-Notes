# 创建一个初始数组
arr = [1, 2, 3]
arr2 = [4,5]

# 添加元素
arr.append(4)  #在列表末尾添加新元素 O(1)
arr.insert(1,1.5) # 在指定位置插入元素，插入后需要移动后续元素，所以需要O(n)
arr[2:2] = [10,20] #切片插入多个元素
arr += arr2 #合并两个数组

#删除元素
last_element = arr.pop() #移除并返回最后一个元素 O(1)
removed = arr.pop(1) #移除并返回索引1处的元素 O(N) 因为后续的元素需要移动
del arr[1]           #移除但不返回删除的元素 O(N)   因为后续的元素需要移动
filtered_arr = [x for x in arr if x%2 !=0] # 用列表进行筛选
arr[1:3] =[] #批量删除
list.remove(x) #移除指定元素的函数 无返回值，但会修改原列表，x如果不在的话会报错 O(n)


#查询元素
element = arr[2] #返回arr中索引为2的元素 O(1)
if 2 in arr:     # 查找是否有2在arr中   O(N)
    index = arr.index(2)  # 返回元素值为2的索引位置
    
#更改元素
arr[0] = 0 #利用索引直接修改元素，O(1)

#切片
lst = [0, 1, 2, 3, 4, 5]

# 提取索引2到4的子列表（不包含索引5）
sub_list = lst[2:5]  # 【2，3，4】

#切片会忽略超出界限的行为只取到结尾

# 复制整个列表（浅拷贝）
copy_list = lst[:]

# 反转列表
reversed_list = lst[::-1]#不会修改原数据，而是返回一个新对象
lst.reverse()#直接修改不返回新列表
reversed(lst)#返回一个迭代器

sub_list = lst[start:end:step]

""" 
start:起始索引（包含该位置）。
end:结束索引（不包含该位置）。
step:步长，支持负数表示反向切片 
"""
lst = [0, 1, 2, 3, 4, 5, 6]
print("索引2到5的子列表:", lst[2:6])   # 输出: [2, 3, 4, 5]
print("步长为2的子列表:", lst[::2])     # 输出: [0, 2, 4, 6]
print("反向列表:", lst[::-1])           # 输出: [6, 5, 4, 3, 2, 1, 0]

#map
# 示例：将列表中的每个数平方
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print("每个元素的平方:", squares)  # 输出: [1, 4, 9, 16]
## lambda x : x * x 定义了一个匿名函数，用于计算每个数的平方 
## map将这个函数作用到numbers中每个元素 返回一个迭代器
## 使用list可以将迭代器变为一个列表

# 示例：过滤出列表中的奇数
numbers = [1, 2, 3, 4, 5, 6]
odds = list(filter(lambda x: x % 2 != 0, numbers))
print("奇数列表:", odds)  # 输出: [1, 3, 5]
## lambda x: x % 2 != 0 用来判断一个数是否为奇数
## filter 会返回那些函数返回True的元素
## 使用list可以将迭代器变为一个列表

#reduce
from functools import reduce

# 示例：计算列表所有数的乘积
numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print("乘积:", product)  # 输出: 24
## lambada a, b : a * b 定义了一个函数，用于将两个数相乘
## reduce 从列表左侧开始，依次将累计的结果与下一个元素进行运算，最终返回整个列表的乘积。

#字典（dict）
# 定义一个字典
person = {"name": "Alice", "age": 25, "city": "New York"}

# 访问字典元素
print(person["name"])  # 输出: Alice

# 添加新键值对
person["gender"] = "Female"

# 删除键值对
del person["age"]

print(person)  # 输出: {'name': 'Alice', 'city': 'New York', 'gender': 'Female'}
#每个键key必须是唯一的，且通常是不可变类型

#使用max找最大值
data = {"a": 10, "b": 25, "c": 15}

max_value = max(data.values())  # 获取最大值
print(max_value)  # 输出: 25
#data.values()获取所有的value值

max_key = max(data,key = data.get) #获取最大值对应的键

#同时获取最大的key和value
max_key = max(data, key=data.get)
max_value = data[max_key]
print(max_key, max_value)  # 输出: b 25

#或者使用items()
max_pair = max(data.items(), key=lambda x: x[1])
print(max_pair)  # 输出: ('b', 25)
#data.items() 返回字典的 key-value 组成的元组列表，如 [('a', 10), ('b', 25), ('c', 15)]。
# max(data.items(), key=lambda x: x[1]) 让 max() 按**value（即 x[1]）排序**，返回 key-value 对。



#循环
"""
for i in range(start, stop, step):
start: 迭代的起始值（包括 start）。
stop: 迭代的终止值（不包括 stop）。
step: 迭代的步长（可以是负数，表示倒序）。
"""

for i in range(5, -1, -1):
    print(i) # 5,4,3,2,1,0