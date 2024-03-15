class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dfs(i, k):
            if i == len(stones)-1:
               return True

            key = (i, k)
            if key not in memo:
                memo[key] = False
                jump = k - 1
                if jump > 0 and (stones[i] + jump) in rev_map:
                    memo[key] |= dfs(rev_map[stones[i] + jump], jump)
                jump = k
                if jump > 0 and (stones[i] + jump) in rev_map:
                    memo[key] |= dfs(rev_map[stones[i] + jump], jump)
                jump = k + 1
                if jump > 0 and (stones[i] + jump) in rev_map:
                    memo[key] |= dfs(rev_map[stones[i] + jump], jump)
            return memo[key]

        memo = {}
        rev_map = {stones[i]: i for i in range(len(stones))}
        return dfs(0, 0)
