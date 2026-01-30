# 卡玛网 105 有向图的完全联通
# 题目链接: https://kamacoder.com/problempage.php?pid=1177

# 方法一：邻接表 + 深度优先搜索（DFS）
from collections import defaultdict
n,k = map(int,input().split())
dic = defaultdict(list)
visited = [False] * (n+1)
for i in range(k):
    start,end = map(int,input().split())
    dic[start].append(end)

def dfs(start):
    for neightbor in dic[start]:
        if not visited[neightbor]:
            visited[neightbor] = True
            dfs(neightbor)

dfs(1)
for i in range(2,n+1):
    if visited[i] == False:
        print(-1)
        exit()
print(1)