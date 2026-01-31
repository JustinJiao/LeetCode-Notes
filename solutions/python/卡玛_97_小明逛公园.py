# 卡玛网 97 小明逛公园
# 题目链接: https://kamacoder.com/problempage.php?pid=1155

#方法一：Floyd算法+动态规划+三维数组
n,m = map(int,input().split())
INF = float('inf')
graph = [[[INF]*  (n+1) for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start,end,val = map(int,input().split())
    graph[start][end][0] = val
    graph[end][start][0] = val

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j][k] = min(graph[i][k][k-1]+graph[k][j][k-1],graph[i][j][k-1])
q = int(input())
for _ in range(q):
    start,end = map(int,input().split())
    result = graph[start][end][n]
    if result == INF:
        print(-1)
    else:
        print(result)

#方法二：Floyd算法+动态规划+二维数组优化
n,m = map(int,input().split())
INF = float('inf')
graph = [[INF]*  (n+1) for _ in range(n+1)]
for _ in range(m):
    start,end,val = map(int,input().split())
    graph[start][end] = val
    graph[end][start] = val

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j],graph[i][j])
q = int(input())
for _ in range(q):
    start,end = map(int,input().split())
    result = graph[start][end]
    if result == INF:
        print(-1)
    else:
        print(result)
