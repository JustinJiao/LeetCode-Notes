# LeetCode No.347 前k个高频元素
# 题目链接: https://leetcode.cn/problems/top-k-frequent-elements/submissions/618765074/

from typing import List

#方法一：字典+反转字典+排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dict_ = defaultdict(int)
        dict2 = defaultdict(list)
        for i in nums:
            dict_[i] +=1
        for key in dict_:
            dict2[dict_[key]].append(key)
        keys = list(dict2.keys())
        keys.sort()
        result = []
        cnt = 0
        while keys and cnt!= k:
            result += dict2[keys[-1]]
            cnt += len(dict2[keys[-1]])
            keys.pop()
        return result[:k]
#方法二：字典+最小堆
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        import heapq
        dict1 = defaultdict(int)
        for i in nums:
            dict1[i] += 1
        heap = []
        for key, freq in dict1.items():
            heapq.heappush(heap,(freq,key))
            if len(heap) > k:
                heapq.heappop(heap)
        result  = [0] *k
        for i in range(k-1,-1,-1):             #不使用append,是因为我们要维护顺序
            result[i] = heapq.heappop(heap)[1] #这里是因为会返回一个元组，也就是freq,和key，我们要key所以要[1]
        return result

            
            
        
            
        