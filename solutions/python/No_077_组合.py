# LeetCode No 77 组合
# 题目链接:https://leetcode.cn/problems/combination-sum/

#回溯模板
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []
        def help(n,k,path,result,startIndex):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(startIndex,n+1):
                path.append(i)
                help(n,k,path,result,i+1)
                path.pop()
        help(n,k,path,result,1)
        return result


#优化回溯模板
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []
        def help(n,k,path,result,startIndex):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(startIndex,n - (k-len(path))+2):
                path.append(i)
                help(n,k,path,result,i+1)
                path.pop()
        help(n,k,path,result,1)
        return result