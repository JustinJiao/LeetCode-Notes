# LeetCode No.017 电话号码的字母组合
# 题目链接: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        path = []
        result = []
        def dfs(startIndex):
            nonlocal dic
            if startIndex == len(digits):
                result.append(''.join(path))
                return
            digit = digits[startIndex]
            letters = dic[digit]
            for i in range(len(letters)):
                path.append(letters[i])
                dfs(startIndex+1)
                path.pop()
        dfs(0)
        return result
