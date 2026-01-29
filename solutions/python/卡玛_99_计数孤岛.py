# 卡玛网 99 计数孤岛
# 题目链接: https://kamacoder.com/problempage.php?pid=1171

#方法一：DFS
n,m = map(int,input().split())
direction = [[1,0],[-1,0],[0,1],[0,-1]]
visted = [[False] * m for _ in range(n)]
graph = []
result = 0

for i in range(n):
    graph.append(list(map(int,input().split())))

def dfs(x,y):
    if visted[x][y] or graph[x][y] == 0:
        return
    visted[x][y] = True
    for i, j in direction:
        next_x = x+i
        next_y = y + j
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        dfs(next_x,next_y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visted[i][j]:
            result +=1
            dfs(i,j)
print(result)

#方法二：BFS
from collections import deque
n,m = map(int,input().split())
direction = [[1,0],[-1,0],[0,1],[0,-1]]
visted = [[False] * m for _ in range(n)]
graph = []
result = 0

for i in range(n):
    graph.append(list(map(int,input().split())))

def dfs(x,y):
    queue = deque()
    queue.append([x,y])
    visted[x][y] = True
    while queue:
        cur_x,cur_y = queue.pop()
        for i,j in direction:
            next_x = cur_x+i
            next_y = cur_y +j
            if next_x < 0 or next_x >=n or next_y<0 or next_y >=m:
                continue
            if not visted[next_x][next_y] and graph[next_x][next_y] == 1:
                visted[next_x][next_y] = True
                queue.append([next_x,next_y])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visted[i][j]:
            result +=1
            dfs(i,j)
print(result)