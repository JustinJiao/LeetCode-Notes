# LeetCode No.994 腐烂的橘子
# 题目链接: https://leetcode.cn/problems/rotting-oranges/description/

# 方法一：广度优先搜索（BFS）
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        queue =deque()
        fresh = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        minutes = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh +=1
        if fresh == 0:
            return 0
        while queue and fresh >0:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                        fresh -= 1
                        grid[nx][ny] =2
                        queue.append((nx,ny))
            minutes +=1
        return minutes if fresh ==0 else -1

