# LeetCode No.1049 最后一块石头的重量二
# 题目链接: https://leetcode.cn/problems/last-stone-weight-ii/description/

from typing import List

#方法一：动态规划一维数组
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        vol = total_sum // 2
        dp = [0] * (vol+1)
        for i in range(len(stones)):
            for j in range(vol,stones[i]-1,-1):
                dp[j] = max(dp[j],stones[i] + dp[j-stones[i]])
        return total_sum - dp[vol]-dp[vol]
#方法二：动态规划+二维数组
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        vol = total_sum // 2
        dp = [[0] * (vol+1) for _ in range(len(stones))]
        for j in range(1,vol+1):
            if j >= stones[0]:
                dp[0][j] = stones[0]
        for i in range(1,len(stones)):
            for j in range(1,vol+1):
                if j >=stones[i]:
                    dp[i][j] = max(dp[i-1][j],stones[i]+dp[i-1][j-stones[i]])
                else:
                    dp[i][j] = dp[i-1][j]
        return total_sum-dp[len(stones)-1][vol]-dp[len(stones)-1][vol]
        

        
        
            
        