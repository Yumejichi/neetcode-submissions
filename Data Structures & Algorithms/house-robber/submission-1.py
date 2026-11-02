class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        # we store max money we can rob do far
        maxMoney = [0] * n
        maxMoney[0] = nums[0]
        maxMoney[1] = max(nums[0],nums[1])

        for i in range(2, n):
            maxMoney[i] = max(maxMoney[i-1], nums[i]+maxMoney[i-2])
            print(maxMoney)

        return maxMoney[-1]

