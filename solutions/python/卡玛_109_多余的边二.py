# 卡玛网 109 多余的边二
# 题目链接: https://kamacoder.com/problempage.php?pid=1182

# 方法一：并查集
from collections import defaultdict
n = int(input())

father = [i for i in range(n+1)]

def find(u):
    if father[u] == u:
        return u
    father[u] = find(father[u])
    return father[u]

def join(x,y):
    a = find(x)
    b = find(y)
    if a==b:
        return
    father[a] = b

def issame(x,y):
    a = find(x)
    b = find(y)
    if a== b:
        return True
    else:
        return False
def delte_edge_still_tree(e):
    global father
    father = [i for i in range(n+1)]
    for i in edge:
        if i == e:
            continue
        x,y = i
        if issame(x,y):
            return False
        else:
            join(x,y)
    return True

edge = [list(map(int,input().split())) for _ in range(n)]
in_degree = defaultdict(int)
for x,y in edge:
    in_degree[y] +=1

vec = []
for i in range(n):
    if in_degree[edge[i][1]] == 2:
        vec.append(i)

if len(vec)>0:
    if delte_edge_still_tree(edge[vec[1]]):
        print(f'{edge[vec[1]][0]} {edge[vec[1]][1]}')
    else:
        print(f'{edge[vec[0]][0]} {edge[vec[0]][1]}')

else:
    father = [i for i in range(n+1)]
    for x,y in edge:
        if issame(x,y):
            print(f'{x} {y}')
        else:
            join(x,y)
    