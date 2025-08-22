# LeetCode No.54 螺旋矩阵
# 题目链接: https://leetcode.cn/problems/spiral-matrix/description/

import ast
import sys
from typing import List

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while left <= right and top <= bottom:
            # 上边界
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # 右边界
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom: #注意这里，如果top > bottom说明这一行已经加过了，就不需要重新加了
                # 下边界
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:#这里也是一样的，如果left>right说明这一列已经加过了，所以不需要再加了
                # 左边界
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

        