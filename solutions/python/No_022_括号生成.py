# LeetCode No.22 括号生成
# 题目链接: https://leetcode.cn/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        def help(left_count,right_count):
            if len(path) == 2 *n:
                result.append(''.join(path))
                return
            if left_count<n:
                path.append('(')
                help(left_count+1,right_count)
                path.pop()
            if right_count < left_count:
                path.append(')')
                help(left_count,right_count+1)
                path.pop()
        help(0,0)
        return result
    