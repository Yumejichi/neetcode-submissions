class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        tank = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            if tank < 0:
                start = i+1
                tank = 0

            total += g - c
        return start if total >= 0 else -1