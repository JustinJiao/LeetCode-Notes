# LeetCode No.216 组合总和三
# 题目链接: https://leetcode.cn/problems/combination-sum-iii/description/

#方法一：回溯
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        def help(n,k,path,result,startIndex):
            if len(path) == k and sum(path)==n:
                result.append(path[:])
                return
            for i in range(startIndex,10):
                path.append(i)
                help(n,k,path,result,i+1)
                path.pop()
            
        help(n,k,path,result,1)
        return result
#优化回溯
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        def help(n,k,path,result,startIndex,currsum):
            if currsum > n:
                return 
            if len(path) == k and currsum == n:
                result.append(path[:])
                return
            for i in range(startIndex,9 - (k - len(path)) + 2):
                currsum += i
                path.append(i)
                help(n,k,path,result,i+1,currsum)
                currsum -= i
                path.pop()
            
        help(n,k,path,result,1,0)
        return result 
            
            
        
            
        