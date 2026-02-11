# LeetCode No.152 乘积最大子数组
# 题目链接: https://leetcode.cn/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp = [1] * len(nums)
        min_dp = [1] * len(nums)

        max_dp[0] = nums[0]
        min_dp[0]=nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            max_dp[i] = max(nums[i],nums[i]*max_dp[i-1],nums[i]*min_dp[i-1])
            min_dp[i] = min(nums[i],nums[i]*max_dp[i-1],nums[i]*min_dp[i-1])
            result = max(max_dp[i],result)
        return result