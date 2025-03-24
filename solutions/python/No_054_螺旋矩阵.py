# LeetCode No.54 螺旋矩阵
# 题目链接: https://leetcode.cn/problems/spiral-matrix/description/

import ast
import sys
from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        starX, starY = 0,0
        offset = 1
        count = 0
        while count < m*n:
            if m*n -len(result) == 1:
                result.append(matrix[m//2][m//2])
                return result
            for i in range(starY,n-offset):
                num = matrix[starX][i] #上边，从左至右
                result.append(num)
                count+=1
                if count == m*n:
                    return result
            for i in range(starX,m-offset): #右边，从上至下
                num = matrix[i][n-offset]
                result.append(num)
                count+=1
                if count == m*n:
                    return result
            for i in range(n-offset,starX,-1):#下边，从右至左
                num = matrix[m-offset][i]
                result.append(num)
                count+=1
                if count == m*n:
                    return result
            for i in range(m-offset,starY,-1):#左边，从下至上
                num = matrix[i][starY]
                result.append(num)
                count+=1
                if count == m*n:
                    return result
            starX+=1
            starY +=1
            offset+=1
            
        
def main():
    n = ast.literal_eval(sys.stdin.read().strip())
    result = spiralOrder(n)
    print(result)
if __name__ == '__main__':
    main()
            
        