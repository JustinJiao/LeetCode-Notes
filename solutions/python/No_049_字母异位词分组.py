# LeetCode No.49 字母异位词分组
# 题目链接: https://leetcode.cn/problems/group-anagrams/description/

from typing import List


#方法一：排序
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        mp = defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())
    
#方法二计数
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        mp = defaultdict(list)
        for st in strs:
            counts = [0]*26
            for ch in st:
                counts[ord(ch)-ord('a')] +=1
            mp[tuple(counts)].append(st)

        return list(mp.values())
        
            
        