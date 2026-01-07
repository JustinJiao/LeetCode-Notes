# LeetCode No.131 分割回文子串
# 题目链接: https://leetcode.cn/problems/palindrome-partitioning/description/

#方法一：回溯
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        def help(startIdex):
            if startIdex == len(s):
                result.append(path[:])
                return
            for i in range(startIdex,len(s)):
                string = s[startIdex:i+1]
                if string == string[::-1]:
                    path.append(string)
                    help(i+1)
                    path.pop()
        help(0)
        return result
        