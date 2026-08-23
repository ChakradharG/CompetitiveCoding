class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(queries)
        k = math.floor(math.sqrt(n))

        l, r = 0, 0
        h, f = [], defaultdict(int)
        ans = [-1 for _ in range(m)]
        for i, query in sorted(enumerate(queries), key=lambda x: (x[1][0]//k, -x[1][1] if (x[1][0]//k)%2 else x[1][1])):   # sort by BLOCK, R
            L, R, thresh = query
            R += 1
            while r < R:
                f[nums[r]] += 1
                heappush(h, (-f[nums[r]], nums[r]))
                r += 1
            while r > R:
                r -= 1
                f[nums[r]] -= 1
                heappush(h, (-f[nums[r]], nums[r]))
            while l < L:
                f[nums[l]] -= 1
                heappush(h, (-f[nums[l]], nums[l]))
                l += 1
            while l > L:
                l -= 1
                f[nums[l]] += 1
                heappush(h, (-f[nums[l]], nums[l]))
            while h and f[h[0][1]] != -h[0][0]:
                heappop(h)
            if -h[0][0] >= thresh:
                ans[i] = h[0][1]

        return ans
