class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def burstLast(l, r, k):
            if l > 0:
                a = nums[l-1]
            else:
                a = 1
            b = nums[k]
            if r < n-1:
                c = nums[r+1]
            else:
                c = 1
            return a * b * c

        n = len(nums)
        if n == 1:
            return nums[0]

        grid = [[0 for r in range(n)] for l in range(n)]
        grid[-1][-1] = nums[-2] * nums[-1]

        for l in reversed(range(n-1)):
            grid[l][l] = burstLast(l, l, l)
            for r in range(l+1, n):
                res = max(
                    burstLast(l, r, l) + grid[l+1][r],
                    grid[l][r-1] + burstLast(l, r, r)
                )
                for k in range(l+1, r):
                    res = max(
                        res,
                        grid[l][k-1] + burstLast(l, r, k) + grid[k+1][r]
                    )
                grid[l][r] = res

        return grid[0][-1]
