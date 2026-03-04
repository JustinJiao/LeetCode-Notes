# LeetCode No.118 杨辉三角
# 题目链接:https://leetcode.cn/problems/pascals-triangle/description/
#方法一：
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = [1] *(i+1)
            for j in range(1,i):
                row[j] = result[i-1][j-1]+result[i-1][j]
            result.append(row)
        return result