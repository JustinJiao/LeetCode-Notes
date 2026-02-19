# LeetCode No.048 旋转图像
# 题目链接: https://leetcode.cn/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top,bottom = 0, n-1
        left,right = 0,n-1
        while top < bottom:
            for j in range(left,right):
                k = j-left

                temp = matrix[top][j]#存储上边

                matrix[top][j] = matrix[bottom-k][left] #左->上

                matrix[bottom-k][left] = matrix[bottom][right-k] #下->左

                matrix[bottom][right-k] = matrix[top+k][right] #右->下

                matrix[top+k][right] = temp

            top +=1
            bottom -=1
            left +=1
            right-=1

        
            
        