# 卡玛网 101 孤岛的总面积
# 题目链接: https://kamacoder.com/problempage.php?pid=1173

#方法一：DFS
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
direction = [(0,1),(0,-1),(1,0),(-1,0)]
visted = [[False]*m for _ in range(n)]
result = 0

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return 0, False
    if visted[x][y] or graph[x][y] == 0:
        return 0, True
    area = 1
    is_close = True
    visted[x][y] = True

    for dx,dy in direction:
        sub_area , sub_close = dfs(x+dx,y+dy)
        area += sub_area
        is_close &= sub_close
    return area, is_close

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visted[i][j]:
            area,is_close = dfs(i,j)
            if is_close:
                result += area

print(result)
