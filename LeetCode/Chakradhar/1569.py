class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def dfs(nums):
            n = len(nums)
            if n < 2:
                return 1

            left, right = [], []
            for i in range(1, n):
                if nums[0] > nums[i]:
                    left.append(nums[i])
                else:
                    right.append(nums[i])

            return (math.comb(n-1, len(left)) * dfs(left) * dfs(right)) % MOD

        MOD = 10**9 + 7
        return dfs(nums) - 1

