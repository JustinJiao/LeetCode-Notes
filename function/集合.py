#创建
List =[1,2,3]
s1 = {1,2,3} #直接创建
s1 = set(List) #可以从列表，元组，字符串等转换
s1 = set("hello")
s1 = set() #创建空的字典

#添加
s1.add(4)
#删除
s1.remove(4) #删除指定元素，若元素不存在则报错
s1.discard(4) #删除元素，不存在不报错
s1.pop()#随机删除一个元素，因为set无序
s1.clear() #清空集合


#集合运算
a = {1, 2, 3}
b = {3, 4, 5}

#并集
print(a | b)  # {1, 2, 3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
#交集
print(a & b)  # {3}
print(a.intersection(b))  # {3}
#差集
print(a - b)  # {1, 2}  (a 中有但 b 中没有)
print(a.difference(b))  # {1, 2}
#对称差集
print(a ^ b)  # {1, 2, 4, 5}  (a 和 b 中不同的元素)
print(a.symmetric_difference(b))  # {1, 2, 4, 5}


#判断关系
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}

print(x.issubset(y))  # True，x 是 y 的子集
print(y.issuperset(x))  # True，y 是 x 的超集
print(x.isdisjoint({4, 5}))  # True，x 和 {4, 5} 没有交集

