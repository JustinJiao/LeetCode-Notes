# 卡玛网 98 可达路径
# 题目链接: https://kamacoder.com/problempage.php?pid=1170

#方法一：邻接矩阵+DFS
n,m = map(int,input().split())
graph = [[0]* (n+1) for _ in range(n+1)]
for _ in range(m):
    node1,node2 = map(int,input().split())
    graph[node1][node2] = 1
 
result = []
path = [1]
def dfs(x,n):
    if x == n:
        result.append(path[:])
        return
    for i in range(1,n+1):
        if graph[x][i] == 1:
            path.append(i)
            dfs(i,n)
            path.pop()
 
dfs(1,n)
if not result:
    print(-1)
else:
    for path in result:
        print(' '.join(map(str,path)))

#方法二：邻接表+DFS
from collections import defaultdict
n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)

result = []
path = [1]
def dfs(x,n):
    if x == n:
        result.append(path[:])
        return
    for i in graph[x]:
        path.append(i)
        dfs(i,n)
        path.pop()

dfs(1,n)
if not result:
    print(-1)
else:
    for path in result:
        print(' '.join(map(str,path)))