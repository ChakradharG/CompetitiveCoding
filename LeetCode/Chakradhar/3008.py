class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def getLPS(string):
            LPS = [0 for _ in range(len(string))]
            p, c = 0, 1
            while c < len(string):
                if string[p] == string[c]:
                    LPS[c] = p + 1
                    p, c = p + 1, c + 1
                else:
                    if p == 0:
                        LPS[c] = 0
                        c += 1
                    else:
                        p = LPS[p - 1]

            return LPS

        def findMatches(string, LPS):
            l1, l2 = len(s), len(string)
            matches = []
            h, n = 0, 0
            while h < l1:
                if s[h] == string[n]:
                    h, n = h + 1, n + 1
                else:
                    if n == 0:
                        h += 1
                    else:
                        n = LPS[n - 1]

                if n == l2:
                    matches.append(h - l2)
                    n = LPS[n - 1]

            return matches

        LPSa = getLPS(a)
        LPSb = getLPS(b)

        mata = findMatches(a, LPSa)
        matb = findMatches(b, LPSb)

        ans = []
        for i in mata:
            j = bisect.bisect_left(matb, i)
            if j > 0 and (i - matb[j-1]) <= k:
                ans.append(i)
            elif j < len(matb) and (matb[j] - i) <= k:
                ans.append(i)

        return ans
