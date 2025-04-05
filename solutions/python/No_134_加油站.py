# LeetCode No.134 加油站
# 题目链接: https://leetcode.cn/problems/gas-station/description/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        cur = 0
        total = 0
        for i in range(len(gas)):
            cur += (gas[i] -cost[i])
            total += (gas[i] - cost[i])
            if cur < 0:
                start = i+1
                cur = 0
        if total <0:
            return -1
        return start
        