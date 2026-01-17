# LeetCode No.051 N皇后
# 题目链接: https://leetcode.cn/problems/n-queens/description/
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = [['.'] * n for _ in range(n)] # 初始化棋盘
        result = []
        row = 0
        def isvalid(chessboard,row,col):
            for i in range(row):#检查同一列是否有皇后
                if chessboard[i][col] == 'Q':
                    return False
            
            i = row -1
            j = col -1
            while i>=0 and j>=0:#检查左上对角线是否有皇后
                if chessboard[i][j] == 'Q':
                    return False
                i-=1
                j-=1
            i = row - 1
            j = col +1
            while i>=0 and j<n:#检查右上对角线是否有皇后
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True
        def help(row):
            if row == n:
                result.append([''.join(r) for r in chessboard])
                return
            for col in range(n):
                if isvalid(chessboard,row,col):
                    chessboard[row][col] = 'Q'
                    help(row+1)
                    chessboard[row][col] = '.'
        help(row)
        return result

            
        