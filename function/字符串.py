##大小写转换

str.lower()	#转换为小写
str.upper()	#转换为大写
str.capitalize()	#首字母大写，其余小写
str.title()	#每个单词首字母大写
str.swapcase()	#大小写互换

s = "hello Python"
print(s.upper())       # "HELLO PYTHON"
print(s.lower())       # "hello python"
print(s.capitalize())  # "Hello python"
print(s.title())       # "Hello Python"
print(s.swapcase())    # "HELLO pYTHON"


##查找&统计
s = "hello world"
print(s.find("o"))       # 4 查找，返回索引，找不到返回-1
print(s.index("o"))      # 4 查找， 返回所以，找不到报错
print(s.count("o"))      # 2 统计 出现的次数
print(s.startswith("he")) # True 是否以he开头 返回 bool
print(s.endswith("ld"))   # True 是否以ld结尾，返回bool


#修改&替换
s = "  hello world  "
print(s.strip())       # "hello world"  移除两端端char，默认为空格
print(s.lstrip())      # "hello world  " 移除左侧的char，默认为空格
print(s.rstrip())      # "  hello world" 移除右侧的char，默认为空格

s2 = "aaahellobbb"
print(s2.strip("ab"))  # "hello"

print(s.replace("world", "Python"))  # "  hello Python  " 替换


##拆分&连接
s = "apple,banana,orange"
print(s.split(","))  # ['apple', 'banana', 'orange'] 按照“，”拆分，返回列表

s2 = "hello\nworld"
print(s2.splitlines())  # ['hello', 'world'] 按照“\n”换行符进行拆分，返回列表

words = ["Python", "is", "fun"]
print(" ".join(words))  # "Python is fun" 用空格连接列表返回字符串


#对齐
s = "hello"
print(s.center(10, "-"))  # "--hello---" 居中对齐用-
print(s.ljust(10, "*"))   # "hello*****" 左对齐用*
print(s.rjust(10, "."))   # ".....hello" 右对齐用.
print("42".zfill(5))      # "00042"      左侧补0


##判断
str.isalpha()	#是否全是字母
str.isdigit()	#是否全是数字
str.isalnum()	#是否全是字母或数字
str.isspace()	#是否全是空白字符
str.islower()	#是否全是小写
str.isupper()	#是否全是大写
str.istitle()	#是否符合标题格式




