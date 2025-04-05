# LeetCode No.860 柠檬水找零
# 题目链接: https://leetcode.cn/problems/lemonade-change/description/

#方法一：贪心
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = [0] * 21
        money[5] = 0
        money[10] = 0
        money[20] = 0
        for i in bills:
            if i == 5:
                money[i] +=1
            elif i == 10:
                money[i] +=1
                money[5] -=1
                if money[5] <0:
                    return False
            else:
                if money[10] >=1 and money[5] >=1:
                    money[10] -=1
                    money[5] -=1
                elif money[10] <1 and money[5] >=3:
                    money[5] -=3
                else:
                    return False
        return True
