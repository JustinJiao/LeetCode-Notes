# 卡玛网 127 骑士的攻击
# 题目链接: https://kamacoder.com/problempage.php?pid=1203

# 方法一：A*算法
import heapq
 
n = int(input())
 
moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
 
def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
 
def bfs(start, end):
    q = [(distance(start, end), start)]
    step = {start: 0}
     
    while q:
        d, cur = heapq.heappop(q)
        if cur == end:
            return step[cur]
        for move in moves:
            new = (move[0] + cur[0], move[1] + cur[1])
            if 1 <= new[0] <= 1000 and 1 <= new[1] <= 1000:
                step_new = step[cur] + 1
                if step_new < step.get(new, float('inf')):
                    step[new] = step_new
                    heapq.heappush(q, (distance(new, end) + step_new, new))
    return -1
                     
for _ in range(n):
    a1, a2, b1, b2 = map(int, input().split())
    print(bfs((a1, a2), (b1, b2)))