# 卡玛网 47 参加科学大会
# 题目链接: https://kamacoder.com/problempage.php?pid=1047

# 方法一：Dijkstra算法+邻接矩阵
# 1、选源点到哪个节点近且该节点未被访问过
# 源点距离源点最近，距离为0，且未被访问。
# 2、该最近节点被标记访问过
# 标记源点访问过
# 3、更新非访问节点到源点的距离（即更新minDist数组

n,m = map(int,input().split())
visted = [False] * (n+1)
mindis = [float('inf')] * (n+1)
mindis[1] = 0
graph = [[float('inf')]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y,val = map(int,input().split())
    graph[x][y] = val

for i in range(1,n+1):
    minval = float('inf')
    cur = -1
    #1选源点
    for j in range(1,n+1):
        if not visted[j] and mindis[j] < minval:
            minval = mindis[j]
            cur = j

    visted[cur] = True

    for k in range(1,n+1):
        if not visted[k] and graph[cur][k]!= float('inf') and graph[cur][k] + mindis[cur] < mindis[k]:
            mindis[k] = graph[cur][k]+mindis[cur]
if mindis[n] != float('inf'):
    print(mindis[n])
else:
    print(-1)

#方法二：Dijkstra算法优化+邻接表
from collections import defaultdict
import heapq

n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    x, y, val = map(int, input().split())
    graph[x].append((y, val))

INF = float('inf')
dist = [INF] * (n+1)
visited = [False] * (n+1)

# 起点
dist[1] = 0
heap = []
heapq.heappush(heap, (0, 1))  # (距离, 节点)

while heap:
    cur_dis, cur_node = heapq.heappop(heap)

    # 跳过过期状态
    if cur_dis > dist[cur_node]:
        continue

    # 标记访问
    visited[cur_node] = True

    for next_node, weight in graph[cur_node]:
        if not visited[next_node]:
            if cur_dis + weight < dist[next_node]:
                dist[next_node] = cur_dis + weight
                heapq.heappush(heap, (dist[next_node], next_node))

if dist[n] == INF:
    print(-1)
else:
    print(dist[n])
