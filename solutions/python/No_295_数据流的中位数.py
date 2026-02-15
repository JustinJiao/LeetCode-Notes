# LeetCode No.295 数据流的中位数
# 题目链接: https://leetcode.cn/problems/find-median-from-data-stream/
import heapq
class MedianFinder:

    def __init__(self):
        self.small = []#存较小的那一部分，用最大堆
        self.large = []#存较大的那一部分，用最小堆

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        cur = -heapq.heappop(self.small)
        heapq.heappush(self.large,cur)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small,-heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) /2
