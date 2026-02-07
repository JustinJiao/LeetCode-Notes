# LeetCode No.22 括号生成
# 题目链接: https://leetcode.cn/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        result = []
        l = ['(',')']
        dic ={'(':0,')':0}
        def help():
            if dic['('] == n:
                count = dic['('] - dic[')']
                for j in range(count):
                    path.append(')')
                result.append(''.join(path))
                for j in range(count):
                    path.pop()
                return
            for i in l:
                if i == ')' and dic['('] == dic[')']:
                    continue
                path.append(i)
                dic[i] +=1
                help()
                path.pop()
                dic[i] -=1
        help()
        return result
    