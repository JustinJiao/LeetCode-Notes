# LeetCode No.32 最长有效括号
# 题目链接: https://leetcode.cn/problems/longest-valid-parentheses/description/

# 方法一：栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        result = 0

        for i,val in enumerate(s):
            if val == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    if stack:
                        result = max(result,i-stack[-1])
                    else:
                        result = max(result,i+1)
                else:
                    stack.append(i)
        return result
            