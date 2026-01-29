# 卡玛网 106 海岸线计算
# 题目链接: https://kamacoder.com/problempage.php?pid=1178

#方法一：正常遍历
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            for dx,dy in direction:
                next_x,next_y = i+dx,j+dy
                if next_x<0 or next_x >=n or next_y <0 or next_y>=m:
                    result+=1
                if 0<=next_x<n and 0<=next_y<m and graph[next_x][next_y] == 0:
                    result += 1
print(result)
