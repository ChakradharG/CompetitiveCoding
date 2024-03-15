class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dfs(i, k):
            if i == len(stones)-1:
               return True

            key = (i, k)
            if key not in memo:
                memo[key] = False
                for jump in [(k - 1), k, (k + 1)]:
                    if jump > 0 and (stones[i] + jump) in rev_map:
                        if dfs(rev_map[stones[i] + jump], jump):
                            memo[key] = True
                            break
            return memo[key]

        memo = {}
        rev_map = {stones[i]: i for i in range(len(stones))}
        return dfs(0, 0)
