# LeetCode No.215 数组中的最大K个元素
# 题目链接: https://leetcode.cn/problems/k-largest-elements-in-an-array/description/

# 方法一：快速选择算法
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        #终极目的是：把数组分区，比pivot小的放在左边，大的放在右边，i就是分割线
        def partition (left,right):
            i = left #下一个放比pivot小的位置
            pivot = nums[right]
            for j in range(left,right):
                if nums[j] <=pivot:
                    nums[i],nums[j] = nums[j],nums[i]
                    i+=1
            nums[i],nums[right] = nums[right],nums[i]
            return i
        n = len(nums)
        target = n -k 
        left, right = 0, len(nums)-1
        while left <= right:
            index = partition(left,right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index +1
            else:
                right = index-1
                
#方法二：最小堆
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
        