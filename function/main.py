#main的主要写法，输入输出


import sys
import ast
ast.literal_eval() ##用于安全解析python的字符串，列表，字典，元组等
sys.stdin.readline()#用于只读取一行输入，适用于逐行处理
sys.stdin.read()#用于读取整个输入，一次性获取所有数据
strip()#去除字符串开头和结尾的空白字符 空格、换行符\n,制表符\t
split()#按空格或指定字符拆分字符串,返回一个列表