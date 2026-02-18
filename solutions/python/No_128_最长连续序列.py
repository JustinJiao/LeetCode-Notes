# LeetCode No.128 最长连续序列
# 题目链接: https://leetcode.cn/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        for num in nums:
            if num -1 not in set_nums:
                cur = num
                length =1

                while cur+1 in set_nums:
                    cur +=1
                    length +=1
                max_length = max(max_length,length)
                if max_length*2 >= len(set_nums):
                    break
        return max_length