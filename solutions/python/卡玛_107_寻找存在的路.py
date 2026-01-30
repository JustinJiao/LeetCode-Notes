# 卡玛网 107 寻找存在的路
# 题目链接: https://kamacoder.com/problempage.php?pid=1179

# 方法一：并查集
n,m = map(int,input().split())
father = [i for i in range(n+1)]
def find(u):
    if father[u] == u:
        return u
    father[u] =find(father[u])
    return father[u]

def join(x,y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    father[a]= b

def issame(x,y):
    a = find(x)
    b = find(y)
    if a==b:
        return True
    else:
        return False

for _ in range(m):
    x,y = map(int,input().split())
    join(x,y)
start,end = map(int,input().split())
if issame(start,end):
    print(1)
else:
    print(0)

    