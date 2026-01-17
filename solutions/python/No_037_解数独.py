# LeetCode No.037 解数独
# 题目链接: https://leetcode.cn/problems/sudoku-solver/description/

from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxs[(i // 3) * 3 + j // 3].add(board[i][j])
        def help():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        box_id = (i // 3) * 3 + j // 3
                        for k in range(1,10):
                            ch = str(k)
                            if (
                               ch not in rows[i] and
                               ch not in cols[j] and 
                               ch not in boxs[box_id]):
                                board[i][j] = ch
                                rows[i].add(ch)
                                cols[j].add(ch)
                                boxs[box_id].add(ch)
                                result = help()
                                if result:
                                    return True
                                board[i][j] = '.'
                                rows[i].remove(ch)
                                cols[j].remove(ch)
                                boxs[box_id].remove(ch)
                        return False
            return True
        help()
                            
            
        