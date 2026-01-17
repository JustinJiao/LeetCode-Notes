# LeetCode No.135 分发糖果
# 题目链接: https://leetcode.cn/problems/candy/description/

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        temp1 = [1]* len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                temp1[i] = temp1[i-1] +1
        temp2 = [1] * len(ratings)
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                temp2[i] = temp2[i+1] +1
        result =0
        for i in range(len(ratings)):
            num = max(temp1[i],temp2[i])
            result += num
        return result
        