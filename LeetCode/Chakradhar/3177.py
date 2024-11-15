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

        row0 = [(0, 0) for _ in range(n+1)]
        row0[-2] = (1, 0)
        row1 = [(0, 0) for _ in range(n+1)]
        row1[-2] = (1, 0)
        for i in reversed(range(n-1)):
            inc, exc = row1[same[i]]
            inc += 1
            exc = max(exc, *row1[diff[i]])
            row1[i] = (inc, exc)

        for _ in range(k):
            for i in reversed(range(n-1)):
                inc, exc = row0[same[i]]
                inc += 1
                exc = max(exc, *row0[diff[i]])
                inc = max(inc, 1 + max(row1[diff[i]]))
                row0[i] = (inc, exc)
            row0, row1 = row1, row0

        return max(row1[0])
