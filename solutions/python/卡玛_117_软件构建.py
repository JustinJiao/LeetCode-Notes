# 卡玛网 117 软件构建
# 题目链接: https://kamacoder.com/problempage.php?pid=1191

# 方法一：拓扑排序
from collections import defaultdict,deque
n,m = map(int,input().split())

#初始化入度数组和map字典进行关系的记录
indegree = [0] * n
dic = defaultdict(list)
for i in range(m):
    x,y = map(int,input().split())
    dic[x].append(y)
    indegree[y] +=1

#找到入度为0的节点
queue = deque()
for i in range(n):
    if indegree[i] ==0:
        queue.append(i)

result =[]
#从上面找到的节点开始遍历
while queue:
    cur = queue.popleft()
    result.append(cur)
    nodes = dic[cur]
    for node in nodes:
        indegree[node] -=1
        if indegree[node] == 0:
            queue.append(node)

if len(result) != n:
    print(-1)
else:
    print(' '.join(map(str,result)))




    