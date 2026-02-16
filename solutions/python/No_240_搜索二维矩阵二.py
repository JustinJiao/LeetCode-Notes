# LeetCode No.240 搜索二维矩阵 II
# 题目链接: https://leetcode.cn/problems/search-a-2d-matrix-ii/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row,col = 0,n-1
        while row<m and col >=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row +=1
            else:
                col-=1
        return False