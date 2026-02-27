# LeetCode No.1004 最大连续1的个数 III
# 题目链接: https://leetcode.cn/problems/max-consecutive-ones-iii/description/

# 方法一：滑动窗口+计数
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        max_length = -1
        for right in range(len(nums)):
            if nums[right] == 0:
                count +=1
            while count > k:
                if nums[left] ==0:
                    count-=1
                left +=1
            max_length = max(max_length,right-left +1)
        return max_length