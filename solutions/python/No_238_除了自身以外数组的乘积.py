# LeetCode No.238 除了自身以外数组的乘积
# 题目链接:https://leetcode.cn/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 数组操作
        #拿到数字，看除了他以外的数字的成绩，放入answer，但时间复杂度是n^2
        #要在n的时间复杂度内完成，那么就需要遍历一遍，不回头遍历
        answer = [1]
        for i in range(1,len(nums)):
            answer.append(answer[i-1]*nums[i-1])
        
        R = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer