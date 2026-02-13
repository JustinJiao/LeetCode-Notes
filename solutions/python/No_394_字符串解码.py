# LeetCode No.394 字符串解码
# 题目链接: https://leetcode.cn/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        for char in s:
            if char!= ']':
                stack.append(char)
            else:
                cur_string = ''
                while stack[-1] !='[':
                    cur_string = stack.pop()+cur_string
                stack.pop() #弹出'['
                cur_num = ''
                while stack and stack[-1].isdigit():
                    cur_num = stack.pop()+cur_num

                stack.append( int(cur_num) * cur_string)

        return "".join(stack)