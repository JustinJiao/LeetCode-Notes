# LeetCode No.74 搜索二维矩阵
# 题目链接: https://leetcode.cn/problems/search-a-2d-matrix/description/

#方法一：剪枝+二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i])-1
            if matrix[i][right] < target:
                continue
            if matrix[i][left] > target:
                return False
            while left <= right:
                mid = (left + right)// 2 
                if matrix[i][mid] > target:
                    right = mid-1
                elif matrix[i][mid] < target:
                    left = mid +1
                else:
                    return True
        return False

#方法二：二维矩阵压缩成一维数组
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 如果不拉直，我们也可以分两步“双重二分”
        # 1. 二分查找那一列，找到目标行 (Vertical Binary Search)
        # 2. 在目标行进行二分 (Horizontal Binary Search)
        
        # 或者直接用最优雅的一维映射法：
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            # 这里的坐标转换是核心
            val = matrix[mid // n][mid % n]
            if val == target: return True
            if val < target: l = mid + 1
            else: r = mid - 1
        return False