class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def manacher(s):
            s = "$#" + "#".join(s) + "#^"
            n = len(s) - 2
            d = [0] * (n+2)
            l, r = 0, 1
            for i in range(1, n+1):
                if i <= r:
                    d[i] = min(r - i, d[l + (r - i)])
                while s[i - d[i]] == s[i + d[i]]:
                    d[i] += 1
                if (i + d[i]) > r:
                    l, r = i - d[i], i + d[i]
            d = d[1:-1]
            n = (n - 1) // 2
            d_ev = [0] * n
            d_od = [0] * n
            for i in range(n):
                d_ev[i] = (d[2*i] - 1) // 2
                d_od[i] = d[2*i + 1] // 2
            return d_ev, d_od

        n = len(s)
        d_ev, d_od = manacher(s)

        intervals = []
        for i in range(n):
            l = i - d_od[i] + 1
            r = i + d_od[i] - 1
            ln = r - l + 1
            if ln >= k:
                x = (ln - k) // 2 # clamp the palindrome to k (or k+1)
                intervals.append((l + x, r - x))
            l = i - d_ev[i]
            r = i + d_ev[i] - 1
            ln = r - l + 1
            if ln >= k:
                x = (ln - k) // 2
                intervals.append((l + x, r - x))
        intervals.sort()

        ans = 0
        pe = -1
        for s, e in intervals:
            if s > pe:
                ans += 1
                pe = e
            else:
                pe = min(pe, e)

        return ans

