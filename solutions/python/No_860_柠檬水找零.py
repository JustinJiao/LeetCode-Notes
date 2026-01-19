# LeetCode No.860 柠檬水找零
# 题目链接: https://leetcode.cn/problems/lemonade-change/description/

#方法一：贪心
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for i in bills:
            if i == 5:
                five +=1
            elif i == 10:
                if five>=1:
                    five -=1
                    ten +=1
                else:
                    return False
            elif i == 20:
                if ten >= 1 and five >=1:
                    ten -=1
                    five -=1
                    twenty +=1
                elif ten<1 and five>=3:
                    five -=3
                    twenty +=1
                else:
                    return False
        return True