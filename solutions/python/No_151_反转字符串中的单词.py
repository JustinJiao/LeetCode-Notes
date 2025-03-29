# LeetCode No.151 反转字符串中的单词
# 题目链接: https://leetcode.cn/problems/reverse-words-in-a-string/description/

#方法一：
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return " ".join(s)

    
            
            
        
            
        