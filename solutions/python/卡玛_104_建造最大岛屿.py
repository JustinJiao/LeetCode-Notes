# 卡玛网 104 建造最大岛屿
# 题目链接: https://kamacoder.com/problempage.php?pid=1176

#方法一：DFS
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visted = [[False] * m for _ in range(n)]
result =0
# print(graph)
dic = {}
direction = [(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y,mark):
    if x <0 or x >= n or y<0 or y>=m:
        return 0
    if graph[x][y] == 0 or visted[x][y]:
        return 0
    count = 1
    visted[x][y] = True
    graph[x][y] = mark
    for dx,dy in direction:
        next_x, next_y = x + dx,y+dy
        count += dfs(next_x,next_y,mark)
    return count
mark = 2
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and not visted[i][j]:
            dic[mark] = dfs(i,j,mark)
            result = max(result,dic[mark])
            mark +=1
# print(dic)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            vistedset = set()
            area = 1
            for dx,dy in direction:
                next_x,next_y = i + dx, j+dy
                if 0<=next_x<n and 0<=next_y<m:
                    if graph[next_x][next_y] !=0 and graph[next_x][next_y] not in vistedset :
                        mark2 = graph[next_x][next_y]
                        vistedset.add(mark2)
                        area += dic[mark2]
            result = max(result,area)
print(result)

