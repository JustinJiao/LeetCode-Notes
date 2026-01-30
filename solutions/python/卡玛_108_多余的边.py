# 卡玛网 108 多余的边
# 题目链接: https://kamacoder.com/problempage.php?pid=1181

# 方法一：并查集
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
    if a == b:
        return
    father[a] = b

def issame(x,y):
    a = find(x)
    b = find(y)
    if a== b:
        return True
    return False

for _ in range(n):
    x,y = map(int,input().split())
    if issame(x,y):
        print(f'{x} {y}')
        exit()
    else:
        join(x,y)
    