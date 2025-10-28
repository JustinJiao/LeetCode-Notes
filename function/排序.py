## sort()和sorted的区别
list.sort()##只能用于列表
list.sorted()##可用于任何迭代对象（list,tiple,dict,set,str）等

##sort
# 原地排序，返回None,修改原对象
#sorted
# 返回一个新的已排序列表 不会修改原对象

#升序
nums = [3, 1, 4, 2]

nums.sort()
print(nums)
# 输出: [1, 2, 3, 4]

nums = [3, 1, 4, 2]
sorted_nums = sorted(nums)
print(sorted_nums)
# 输出: [1, 2, 3, 4]
print(nums)
# 原 nums 不变: [3, 1, 4, 2]


#降序
nums = [3, 1, 4, 2]

nums.sort(reverse=True)
print(nums)
# 输出: [4, 3, 2, 1]

nums = [3, 1, 4, 2]
sorted_nums = sorted(nums, reverse=True)
print(sorted_nums)
# 输出: [4, 3, 2, 1]

#用key自定义排序规则
words = ['apple', 'banana', 'kiwi', 'pear']
words.sort(key=len)
print(words)
# 输出: ['kiwi', 'pear', 'apple', 'banana']

#按照字符串最后一个排序
words = ['apple', 'banana', 'kiwi', 'pear']
sorted_words = sorted(words, key=lambda x: x[-1])
print(sorted_words)
# 输出: ['banana', 'apple', 'pear', 'kiwi']


students = [('Tom', 90), ('Jerry', 95), ('Bob', 85)]

# 按分数从高到低排序
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)
# 输出: [('Jerry', 95), ('Tom', 90), ('Bob', 85)]



# 字典排序
scores = {'Tom': 90, 'Jerry': 95, 'Bob': 85}

# 按值排序
sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_items)
# 输出: [('Jerry', 95), ('Tom', 90), ('Bob', 85)]

