class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def dfs(i, x, s):
            if s == k:
                return (2**(n-x))
            if i == n or s > k:
                return 0
            key = (i, x, s)
            if key not in memo:
                memo[key] = (dfs(i+1, x, s) +
                    dfs(i+1, x+1, s+nums[i]))
            return memo[key]

        memo = {}
        return dfs(0, 0, 0) % (10**9 + 7)
