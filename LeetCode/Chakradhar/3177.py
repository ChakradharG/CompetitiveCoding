class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        d = {}
        same = [n for _ in range(n)]
        for i in reversed(range(n)):
            same[i] = d.get(nums[i], n)
            d[nums[i]] = i

        h = []
        diff = [n for _ in range(n)]
        for i in reversed(range(n)):
            while h and h[0][1] == nums[i]:
                heappop(h)
            if h:
                diff[i] = h[0][0]
            heappush(h, (i, nums[i]))

        def dfs(i, k):
            if i == (n - 1):
                return 1, 0 # including this, skipping this
            elif i == n:
                return 0, 0

            key = (i, k)
            if key not in memo:
                x, y = dfs(same[i], k)
                inc = 1 + x  # include this and go to next index that is same as this
                exc = y
                x, y = dfs(diff[i], k)
                exc = max(exc, x, y) # skip this
                if k > 0:
                    x, y = dfs(diff[i], k-1)
                    inc = max(
                        inc,
                        1 + x,  # include this
                        1 + y   # include this
                    )
                memo[key] = [inc, exc]
            return memo[key]

        memo = {}
        return max(dfs(0, k))
