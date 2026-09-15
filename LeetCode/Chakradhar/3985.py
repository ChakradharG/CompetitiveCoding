class Solution:
    def getSum(self, nums: List[int]) -> int:
        def manacher(l0):
            ll = [0] * (len(l0)*2 + 3)
            ll[0] = -1
            ll[-1] = -2
            for i in range(len(l0)):
                ll[2*i+2] = l0[i]
            n = len(ll) - 2
            d = [0] * (n+2)
            l, r = 0, 1
            for i in range(1, n+1):
                if i <= r:
                    d[i] = min(r - i, d[l + (r - i)])
                while ll[i - d[i]] == ll[i + d[i]]:
                    d[i] += 1
                if (i + d[i]) > r:
                    l, r = i - d[i], i + d[i]
            return d[1:-1]

        n = len(nums)
        d = manacher(nums)
        d_ev = [0] * n
        d_od = [0] * n
        for i in range(n):
            d_ev[i] = (d[2*i] - 1) // 2
            d_od[i] = d[2*i + 1] // 2

        pref = [0] * (n+1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]

        ans = 0
        for i in range(n):
            l = i - d_od[i] + 1
            r = i + d_od[i] - 1
            ans = max(ans, pref[r+1] - pref[l])
            l = i - d_ev[i]
            r = i + d_ev[i] + 1
            ans = max(ans, pref[r+1] - pref[l])

        return ans

