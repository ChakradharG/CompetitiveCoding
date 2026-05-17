class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        p, MOD = 2**29 - 1, 10**9 + 7
        n = len(nums)
        ps = [1]
        pref = [0]
        for i in range(n):
            ps.append((ps[-1] * p) % MOD)
            h = (pref[-1] + (nums[i] * ps[i])) % MOD
            pref.append(h)

        def getH(st, en):
            return (ps[n-en] * (pref[en] - pref[st])) % MOD

        def poss(ln):
            d = defaultdict(int)
            ones = 0
            for i in range(n-ln+1):
                h = getH(i, i+ln)
                d[h] += 1
                if d[h] == 1:
                    ones += 1
                elif d[h] == 2:
                    ones -= 1
            return ones > 0

        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            if poss(m):
                r = m
            else:
                l = m + 1

        return r
