# LeetCode No.93 复原IP地址
# 题目链接: https://leetcode.cn/problems/restore-ip-addresses/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        result = []
        def check(l):
            if int(l[0]) == 0 and len(l) > 1: return False
            if int(l) > 255 or int(l) < 0:
                return False
            return True
        def help(startIndex):
            if len(path) == 4 and startIndex == len(s):
                result.append('.'.join(path[:]))
                return
            if len(path) > 4:
                return
            for i in range(startIndex,len(s)):
                string = s[startIndex:i+1]
                if check(string):
                    path.append(string)
                    help(i+1)
                    path.pop()
        help(0)
        return result
            