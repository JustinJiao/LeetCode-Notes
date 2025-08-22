# LeetCode No.59 螺旋矩阵二
# 题目链接: https://leetcode.cn/problems/spiral-matrix-ii/description/

import sys
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = []
        for _ in range(n):
            row = [0]*n
            result.append(row)
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        count = 1
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                result[top][i] = count
                count +=1
            top+=1
            for i in range(top,bottom+1):
                result[i][right] = count
                count+=1
            right -= 1
            if top <= bottom:
                for i in range(right,left-1,-1):
                    result[bottom][i] = count
                    count+=1
                bottom -=1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    result[i][left] = count
                    count +=1
                left +=1
        return result
        