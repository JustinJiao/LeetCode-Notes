# LeetCode No.503 下一个更大元素二
# 题目链接: https://leetcode.cn/problems/next-greater-element-ii/description/

#方法一：单调栈
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1]*len(nums)
        stack = [0]
        longnums = nums*2
        for i in range(1,len(longnums)):
            if longnums[i] <= longnums[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)>0 and longnums[i] > longnums[stack[-1]]:
                    if stack[-1] >= len(nums):
                        index = stack[-1]-len(nums)
                    else:
                        index = stack[-1]
                    if result[index] == -1:
                        result[index] = longnums[i]
                    stack.pop()
                stack.append(i)
        return result