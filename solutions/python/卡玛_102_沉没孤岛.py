# 卡玛网 102 沉没孤岛
# 题目链接: https://kamacoder.com/problempage.php?pid=1174

#方法一：DFS
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visted = [[False] * m for _ in range(n)]
direction = [(1,0),(-1,0),(0,-1),(0,1)]

def dfs(x,y):
    if x< 0 or x >=n or y<0 or y >= m:
        return [],False
    if graph[x][y] == 0 or visted[x][y]:
        return [],True
    is_close = True
    cor = []
    visted[x][y]= True
    cor.append((x,y))
    if x == 0 or x == n-1 or y ==0 or y==m-1:
        is_close = False
    for dx,dy in direction:
        next_x = x + dx
        next_y = y + dy
        sub_cor, sub_close = dfs(next_x,next_y)
        cor += sub_cor
        is_close &= sub_close
    return cor,is_close

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visted[i][j]:
            cor,is_close = dfs(i,j)
            if is_close:
                for x,y in cor:
                    graph[x][y] = 0
for row in graph:
    print(' '.join(map(str,row)))