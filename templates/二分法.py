from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right) // 2 ## 这里是//是向下取整，
            if nums[middle] > target:    ## 如果是/的话就是取float数
                right = middle-1
            elif nums[middle] < target:
                left = middle +1
            else:
                return middle
        return -1