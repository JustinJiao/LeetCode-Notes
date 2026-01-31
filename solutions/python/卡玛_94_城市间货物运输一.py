# 卡玛网 94 城市间货物运输一
# 题目链接: https://kamacoder.com/problempage.php?pid=1152

#方法一：bellman-ford算法
n,m = map(int,input().split())
edges = []
INF = float('inf')
mindis = [INF] *(n+1)
mindis[1] = 0
for _ in range(m):
    x,y,val = map(int,input().split())
    edges.append((x,y,val))
for _ in range(n-1):
    update = False
    # 松弛操作
    for x,y,val in edges:
        if mindis[x] != INF and mindis[y] > mindis[x]+val :
            mindis[y] = mindis[x]+val
            update = True
    if not update:
        break
# 检测负权环
for x, y, val in edges:
    if mindis[x] != INF and mindis[x] + val < mindis[y]:
        print("negative cycle")
        exit()

if mindis[n] == INF:
    print('unconnected')
else:
    print(mindis[n])

#方法二：bellman-ford算法优化
from collections import defaultdict,deque
n,m = map(int,input().split())
graph = defaultdict(list)
INF = float('inf')
mindis = [INF] *(n+1)
mindis[1] = 0
for _ in range(m):
    start,des,weight = map(int,input().split())
    graph[start].append((des,weight))

queue = deque()
queue.append(1)
inqueue = [False] *(n+1)# 记录节点是否在队列中
inqueue[1] = True
relax_time = [0] *(n+1)
while queue:
    cur = queue.popleft()
    inqueue[cur] = False
    for des,weight in graph[cur]:
        if mindis[des] > mindis[cur] + weight:
            mindis[des] = mindis[cur] + weight
            if not inqueue[des]:
                queue.append(des)
                relax_time[des] +=1
                inqueue[des] = True
            if relax_time[des] > n:# 出现负权环
                print('negative cycle')
                exit()



if mindis[n] == INF:
    print('unconnected')
else:
    print(mindis[n])
