class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        m = {chr(i+97):i for i in range(26)}
        last = [-1] * 26
        pref = []
        for i, c in enumerate(s):
            last[m[c]] = i
            cur = [-1]
            for j in range(26):
                if last[j] != -1 and last[j] != i:
                    cur.append(last[j])
            cur.append(i)
            pref.append(sorted(cur, reverse=True))

        last = [n] * 26
        suff = [None] * n
        for i in reversed(range(n)):
            c = s[i]
            last[m[c]] = i
            cur = [n]
            for j in range(26):
                if last[j] != n and last[j] != i:
                    cur.append(last[j])
            cur.append(i)
            suff[i] = sorted(cur)

        ans = 0
        for j in range(n-1):
            x = min(len(pref[j]), len(suff[j+1]))
            for jj in range(x-1):
                a = pref[j][jj] - pref[j][jj+1]
                b = suff[j+1][jj+1] - suff[j+1][jj]
                ans += a*b

        return ans

