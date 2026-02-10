# LeetCode No 79 单词搜索
# 题目链接: https://leetcode.cn/problems/word-search/

#方法一：递归回溯+dfs
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        m,n = len(board),len(board[0])
        def dfs(x,y,k):
            if k == len(word)-1:
                return True

            temp = board[x][y]
            board[x][y] = '#'
            
            for dx,dy in directions:
                next_x,next_y = x+dx,y+dy
                if 0<=next_x<m and 0<=next_y<n:
                    if word[k+1] == board[next_x][next_y]:
                        if dfs(next_x,next_y,k+1):
                            return True
            board[x][y] = temp
            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
