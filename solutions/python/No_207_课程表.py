# LeetCode No.207 课程表
# 题目链接: https://leetcode.cn/problems/course-schedule/description/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict,deque
        indegree = [0] * numCourses 
        dic = defaultdict(list)
        for x,y in prerequisites:
            dic[y].append(x)
            indegree[x] +=1
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        count = 0
        while queue:
            cur = queue.popleft()
            count +=1
            for nex in dic[cur]:
                indegree[nex] -=1
                if indegree[nex] == 0:
                    queue.append(nex)
        return count == numCourses
