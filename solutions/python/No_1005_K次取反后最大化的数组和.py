# LeetCode No.1005 K次取反后最大化的数组和
# 题目链接: https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/description/


from typing import List
from collections import Counter
#方法一：贪心+字典
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if freq[i]:
                ops = min(k, freq[i])
                ans += -i * ops * 2
                freq[i] -= ops
                freq[-i] += ops
                k -= ops
                if k == 0:
                    break
        
        if k > 0 and k % 2 == 1 and not freq[0]:
            for i in range(1, 101):
                if freq[i]:
                    ans -= i * 2
                    break
        
        return ans

#方法二：贪心+排序
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        result = 0
        while k > 0:
            nums.sort()
            nums[0] = -nums[0]
            k-=1
        for i in nums:
            result += i
        return result
            
        