class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0

        for i in range(k+1):#k+1 flights are possible for k stops
            newCosts = costs.copy()

            for s,d,p in flights:
                if costs[s] == float("inf"):
                    continue
                if costs[s] + p < newCosts[d]:
                    newCosts[d] = costs[s] + p
            costs = newCosts
        return -1 if costs[dst] == float("inf") else costs[dst]
             