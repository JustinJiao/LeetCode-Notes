# LeetCode No.017 电话号码的字母组合
# 题目链接: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        path = []
        result =[]
        stringmap = [
            [],[],
            ['a','b','c'],
            ['d','e','f'],
            ['g','h','i'],
            ['j','k','l'],
            ['m','n','o'],
            ['p','q','r','s'],
            ['t','u','v'],
            ['w','x','y','z'],
        ]
        def help(s,result,digits,index):
            nonlocal stringmap
            if index == len(digits):
                result.append(s)
                return
            digit = int(digits[index])
            letter = stringmap[digit]
            for i in range(len(letter)):
                s += letter[i]
                help(s,result,digits,index+1)
                s = s[:-1]
        help('',result,digits,0)
        return result
            
