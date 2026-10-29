from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        prerequisiteDict = defaultdict(list)

        for course, pre in prerequisites:
            prerequisiteDict[pre].append(course)
            indegrees[course] += 1

        res = 0

        q = deque()
        print(indegrees)
        for course in range(numCourses):
            print(course)
            if indegrees[course] == 0:
                q.append(course)
                res += 1

        while q:
            curr = q.popleft()
            for course in prerequisiteDict[curr]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)
                    res += 1
        return res == numCourses
        


