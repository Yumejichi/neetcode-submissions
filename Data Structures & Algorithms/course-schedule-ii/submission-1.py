from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        indegrees = [0] * numCourses
        prerequisitesMap = defaultdict(list)

        for course, pre in prerequisites:
            indegrees[course] += 1
            prerequisitesMap[pre].append(course)
        q = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)
        while q:
            curr = q.popleft()
            res.append(curr)
            for course in prerequisitesMap[curr]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)
        return res if len(res) == numCourses else []
