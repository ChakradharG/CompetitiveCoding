class Solution:
    def minSelection(self, availableIntervals: List[List[int]], targetIntervals: List[List[int]]) -> int:
        m = len(availableIntervals)
        availableIntervals.sort(key=lambda x: x[0])
        targetIntervals.sort(key=lambda x: x[0])

        newt = []
        ps, pe = targetIntervals[0]
        for s, e in targetIntervals + [[inf, inf]]:
            if s > pe:
                newt.append((ps, pe))
                ps, pe = s, e
            else:
                pe = max(pe, e)

        r = -inf
        ans = 0
        h = []
        i = 0
        for s, e in newt:
            x = max(r, s)
            while r < e:
                while i < m and availableIntervals[i][0] <= x:
                    ns, ne = availableIntervals[i]
                    if ne >= x:
                        heappush(h, (-ne, ns))
                    i += 1

                while h and -h[0][0] < x:
                    heappop(h)
                if not h:
                    return -1

                y = -heappop(h)[0]
                ans += 1
                r = max(r, y)
                x = r
        return ans

