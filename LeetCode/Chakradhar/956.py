class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        @cache
        def dfs(i, diff):
            if i == n:
                return -inf if diff else 0
            return max(
                dfs(i+1, diff),
                rods[i] + dfs(i+1, diff+rods[i]),
                dfs(i+1, diff-rods[i]),
            )

        n = len(rods)
        return dfs(0, 0)

