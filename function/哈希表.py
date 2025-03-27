#字典
#需要根据唯一键快速检索数据
#当数据顺序不重要时

# 定义字典
my_dict = {'apple': 1, 'banana': 2}

# 添加或更新键值对
my_dict['orange'] = 3

# 访问值
value = my_dict.get('apple')  # 如果键不存在，返回None或指定默认值

# 删除键值对
del my_dict['banana']

# 遍历字典
for key, value in my_dict.items():
    print(key, value)

ord()#用于返回传入的字符串的Unicode编码


#这个defaultdict是创建一个默认的dic，如果不存在的key将默认为int 也就0
from collections import defaultdict
s = defaultdict(int)
t = defaultdict(int)

#这个专门用于统计哈希对象
from collections import Counter
s1 = Counter(s)
t1 = Counter(t)


##defaultdic用于分组场景，当访问不存在的键的时候，自动创建一个空列表
##Counter主要用于计数，统计各个元素出现的次数。

#哈希的键必须是不可变的，所以可以使用tuple把list变为tuple作为键存入
