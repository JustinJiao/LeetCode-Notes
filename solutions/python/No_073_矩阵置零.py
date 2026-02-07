# LeetCode No.73 矩阵置零
# 题目链接: https://leetcode.cn/problems/set-matrix-zeroes/description/

#方法一：标准方法
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = any(matrix[0][j]==0 for j in range(n))
        first_col = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] =0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0

#方法二：个人方法
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        def help(x,y):
            for i in range(m):
                if matrix[i][y] != 0:
                    matrix[i][y] = 'a'
            for j in range(n):
                if matrix[x][j] != 0:
                    matrix[x][j] = 'a'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    help(i,j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
        
        