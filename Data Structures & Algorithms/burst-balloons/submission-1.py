class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def dfs(left, right):
            # No balloons between these boundaries.
            if right == left + 1:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            best = 0
            for i in range(left + 1, right):
                # Save balloon i until last in this interval.
                coins = (
                    dfs(left, i)
                    + dfs(i, right)
                    + nums[left] * nums[i] * nums[right]
                )
                best = max(best, coins)

            memo[(left, right)] = best
            return best

        return dfs(0, len(nums) - 1)