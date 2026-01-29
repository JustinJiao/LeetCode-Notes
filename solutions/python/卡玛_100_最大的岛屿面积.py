# 卡玛网 99 计数孤岛
# 题目链接: https://kamacoder.com/problempage.php?pid=1171

#方法一：DFS
n,m = map(int,input().split())
graph = []
direction = [[1,0],[-1,0],[0,1],[0,-1]]
result = 0
for _ in range(n):
    graph.append(list(map(int,input().split())))
visted = [[False] * m for _ in range(n)]

def dfs(x,y):
    if visted[x][y] or graph[x][y] == 0:
        return 0
    visted[x][y] = True
    area = 1
    for i,j in direction:
        next_x = x + i
        next_y = y + j
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >=m:
            continue
        area += dfs(next_x,next_y)
    return area


result = 0
for x in range(n):
    for y in range(m):
        if not visted[x][y] and graph[x][y] ==1:
            result = max(result,dfs(x,y))

print(result)

    

#方法二：BFS
from collections import deque
n,m = map(int,input().split())
graph = []
direction = [[1,0],[-1,0],[0,1],[0,-1]]
result = 0
for _ in range(n):
    graph.append(list(map(int,input().split())))
visted = [[False] * m for _ in range(n)]

def bfs(x,y):
    area = 0
    visted[x][y] = True
    queue = deque()
    queue.append((x,y))
    while queue:
        cur_x,cur_y = queue.pop()
        area +=1
        for i, j in direction:
            next_x = cur_x + i
            next_y = cur_y + j
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >=m:
                continue
            if not visted[next_x][next_y] and graph[next_x][next_y] == 1:
                visted[next_x][next_y] = True
                queue.append((next_x,next_y))
    return area

result = 0
for x in range(n):
    for y in range(m):
        if not visted[x][y] and graph[x][y] ==1:
            result = max(result,bfs(x,y))

print(result)

    