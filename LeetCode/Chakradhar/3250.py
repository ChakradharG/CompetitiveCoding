class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        def dfs(i, a1, a2):
            if i == len(nums):
                return 1

            key = (i, a1, a2)
            if key not in memo:
                memo[key] = 0
                for x in range(a1, nums[i]+1):
                    y = nums[i] - x
                    if y > a2:
                        continue
                    memo[key] = (memo[key] + dfs(i+1, x, y)) % MOD

            return memo[key]

        memo = {}
        ans = 0
        MOD = 10**9 + 7
        for i in range(nums[0]+1):
            ans = (ans + dfs(1, i, nums[0]-i)) % MOD

        return ans
