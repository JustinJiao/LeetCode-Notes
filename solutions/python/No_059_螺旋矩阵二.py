# LeetCode No.59 螺旋矩阵二
# 题目链接: https://leetcode.cn/problems/spiral-matrix-ii/description/

import sys
from typing import List

def generateMatrix( n: int) -> List[List[int]]:
        nums = []
        for _ in range(n):
            row = [0] * n
            nums.append(row)
        starX, starY = 0,0
        offset = 1
        count =1
        loop = n//2
        while(loop):
            for i in range(starX,n-offset):##上边，从左至右
                nums[starX][i] = count
                count +=1
            for i in range(starY,n-offset):##右边，从上至下
                nums[i][n-offset] = count
                count += 1
            for i in range(n-offset,starY,-1):
                nums[n-offset][i] = count ##下边，从右至左
                count+=1
            for i in range(n-offset,starX,-1): ##左边，从上至下
                nums[i][starY] = count
                count+=1
            starX +=1
            starY +=1
            offset +=1
            loop -=1
        if n%2 !=0:
            nums[n//2][n//2] = count    
        return nums
        
def main():
    n = int(sys.stdin.readline().strip())
    result = generateMatrix(n)
    print(result)
if __name__ == '__main__':
    main()
            
        