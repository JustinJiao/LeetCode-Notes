# 卡玛网 53 寻宝
# 题目链接: https://kamacoder.com/problempage.php?pid=1053

#方法一 ：邻接矩阵 + prime算法  

n,m = map(int,input().split())
graph = [[float('inf')]*(n+1)for _ in range(n+1)]

#存图
for _ in range(m):
    start,end,val = map(int,input().split())
    graph[start][end] = val
    graph[end][start] = val

#声明需要的列表
isTree = [False] * (n+1)
mindistance = [float('inf')] * (n+1)

# 遍历每一个节点
for i in range(1,n):
    #1.选距离生成树最近节点
    minvalue = float('inf')
    cur = 1
    for j in range(1,n+1):
        if not isTree[j] and mindistance[j] < minvalue:
            minvalue = mindistance[j]
            cur = j


    # 2. 最近节点加入生成树
    isTree[cur] = True


    # 更新非生成树节点到生成树的距离（即更新minDist数组）
    for k in range(1,n+1):
        if not isTree[k] and graph[cur][k] < mindistance[k]:
            mindistance[k] = graph[cur][k]

#统计结果
result = 0
for i in range(2,len(mindistance)):
    result += mindistance[i]
print(result)

# 方法二：并查集+Kruskal算法
n, m = map(int,input().split())
edges = []
for _ in range(m):
    x,y,val = map(int,input().split())
    edges.append((x,y,val))
edges.sort(key = lambda x: x[2])

father = [i for i in range(n+1)]
def find(u):
    if father[u] == u:
        return u
    father[u] = find(father[u])
    return father[u]

def join(x,y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    father[a] = b

def issame(x,y):
    a = find(x)
    b = find(y)
    if a == b:
        return True
    else:
        return False

result = 0

for edge in edges:
    x,y,val = edge
    if not issame(x,y):
        join(x,y)
        result += val

print(result)