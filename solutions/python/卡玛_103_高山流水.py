# 卡玛网 103 高山流水
# 题目链接: https://kamacoder.com/problempage.php?pid=1175

#方法一：DFS
n,m = map(int,input().split())
graph = [list(map(int,input().split()))for _ in range(n)]
firstboard = [[False] * m for _ in range(n)]
secondboard = [[False] * m for _ in range(n)]
direction = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(x,y,board):
    if x < 0 or x >= n or y <0 or y>= m:
        return
    if board[x][y] == True:
        return
    board[x][y]= True
    for dx,dy in direction:
        next_x, next_y = x+dx,y+dy
        if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] >= graph[x][y]:
            dfs(next_x,next_y,board)

for i in range(n):
    dfs(i,0,firstboard)
    dfs(i,m-1,secondboard)
for j in range(m):
    dfs(0,j,firstboard)
    dfs(n-1,j,secondboard)
for i in range(n):
    for j in range(m):
        if firstboard[i][j] and secondboard[i][j]:
            print(f'{i} {j}')