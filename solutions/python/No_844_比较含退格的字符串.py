# LeetCode No.844 比较含退格的字符串
# 题目链接: https://leetcode.cn/problems/backspace-string-compare/description/

from typing import List

#方法一：快慢指针
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def r (s:str) -> str:
            ss = list(s)
            left = 0
            for right in range(len(ss)):
                if ss[right] != "#":
                    ss[left] = ss[right]
                    left +=1
                elif left >0:
                    left -=1
            ss = ss[:left]
            return "".join(ss)
        return r(s) == r(t)
#方法2：逆序双指针    
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1
        skips = 0
        skipt = 0
        while i >= 0 or j >= 0:#注意这里是or，因为可能长度不同
            while i >=0:
                if s[i] == '#':#如果是#，就skip+1，然后i往前走
                    i-=1
                    skips +=1
                elif skips >0:#如果有skip说明需要跳，所以i继续往前走
                    i-=1
                    skips-=1
                else:
                    break#跳完了，现在没有skip，也就是目前就需要定位在这里
            while j >=0:
                if t[j] == '#':
                    j-=1
                    skipt +=1
                elif skipt >0:
                    j-=1
                    skipt-=1
                else:
                    break
            if i>=0 and j >=0:#如果两个的位置都大于0，那么就对比两个的字母是否一致
                if s[i] != t[j]:
                    return False
            elif i >=0 or j>=0:#如果不是两个都大于0，而是有一个大于0，而另一个不大于0，那么说明此时一个还有字母，另一个没了，肯定是不一样的
                return False
            i-=1
            j-=1
        return True
        
        