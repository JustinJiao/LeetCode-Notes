# 卡玛网 110 字符串迁移
# 题目链接: https://kamacoder.com/problempage.php?pid=1183

# 方法一：BFS（广度优先搜索）
from collections import deque
n = int(input())
start,end = input().split()
stringlist = [input() for _ in range(n)]
visted = [False for _ in range(n)]
if start == end:
    print(0)
    exit()

def check(s1,s2):
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff +=1
    return diff == 1

queue = deque()
queue.append((start,1))
while queue:
    curstr,step = queue.popleft()
    if check(curstr,end):
        print(step+1)
        exit()
    for i in range(n):
        if not visted[i] and check(curstr,stringlist[i]):
            visted[i] = True
            queue.append((stringlist[i],step+1))

print(0)
    