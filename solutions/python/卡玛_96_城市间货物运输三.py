# 卡玛网 96 城市间货物运输三
# 题目链接: https://kamacoder.com/problempage.php?pid=1154

# 方法一：bellman-ford算法
n,m = map(int,input().split())
edges = []
INF = float('inf')
mindis = [INF] *(n+1)
for _ in range(m):
    x,y,val = map(int,input().split())
    edges.append((x,y,val))
start,end,k = map(int,input().split())
mindis[start] = 0
for _ in range(k+1):
    update = False
    # 松弛操作
    mindis_copy = mindis.copy()
    for x,y,val in edges:
        if mindis_copy[x] != INF and mindis[y] > mindis_copy[x]+val :
            mindis[y] = mindis_copy[x]+val
            update = True
    if not update:
        break



if mindis[end] == INF:
    print('unreachable')
else:
    print(mindis[end])
#方法二：bellman-ford算法优化
