# LeetCode No.904 水果成篮
# 题目链接: https://leetcode.cn/problems/fruit-into-baskets/description/

from typing import Counter, List

#方法一：双指针（滑动窗口）
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = Counter() ##创建哈希表
        left = ans = 0
        for right, x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
        
            
        