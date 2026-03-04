# LeetCode No.051 N皇后
# 题目链接: https://leetcode.cn/problems/n-queens/description/
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        graph = [['.']*n for _ in range(n)]
        col_set = set()
        left = set()
        right = set()
        def help(row):
            if row == n:
                result.append([''.join(row) for row in graph])
                return
            for col in range(n):
                if col in col_set or row-col in left or row+ col in right:
                    continue
                col_set.add(col)
                left.add(row-col)
                right.add(row+col)
                graph[row][col] = 'Q'
                help(row +1)
                graph[row][col] = '.'
                right.remove(row+col)
                left.remove(row-col)
                col_set.remove(col)
        help(0)
        return result

            

            
        