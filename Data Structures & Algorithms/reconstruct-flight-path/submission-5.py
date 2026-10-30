from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        HOU: JFK
        SEA: JFK
        JFK: (HOU, visited), SEA


JFK -> HOU -> JFK -> SEA -> JFK
        '''
        adjList = defaultdict(list)
        for u, v in sorted(tickets,reverse=True):
            adjList[u].append(v)


        origin = "JFK"
        n = len(tickets)
        path = ["JFK"]
        # def backtrack(node):
        #     if len(path) == n + 1:
        #         print(path)
        #         return True
        #     for index, (neighbor, visited) in enumerate(adjList[node]):
        #         if visited == False:
        #             path.append(neighbor)
        #             adjList[node][index][1] = True
        #             if backtrack(neighbor):
        #                 return
        #             path.pop()
        #             adjList[node][index][1] = False
        # backtrack(origin)
        res = []
        def dfs(node):
            while adjList[node]:
                dfs(adjList[node].pop())
            res.append(node)

        dfs("JFK")
        return res[::-1]