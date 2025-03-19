# 二分法
##二分法的前提是数组为有序数组，同时强调数组中无重复元素，
# 因为一旦有重复元素，使用二分法返回的下标可能不唯一.
##有重复元素的情况下，可以使用左右界限的方式进行查找左右边界。


#常见的题型
#No.704二分查找 最经典的题目

#No.35 搜素插入位置：
## 这个题目主要是在最后一步的时候，确认如果没有目标数字的情况下，怎么返回
## 可以寻找其中的规律，发现最后是right +1 

#No.34在排序数组中查找元素的第一个和最后一个位置
##这个题目就是主要是用两次二分查找分别找寻左右界限，
##如果是找左界限的话，当找到数字之后，就还需要right向左移一个，查找是否还有相同的数字
##同理找右界限，在找到之后，先记录mid位置，然后右移左指针。

#No.69 x的平方根
##这道题因为是向下取整，所以在左指针移动的时候需要先记录左指针的数字
##因为左指针移动说明target比当前的mid要大，所以要先记录左指针的数值。

#No.367 有效的完全平方数
##这个也是类似于经典的二分法


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
            

