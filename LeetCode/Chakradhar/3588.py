class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        if len(coords) < 3:
            return 0

        xes = defaultdict(list)
        yes = defaultdict(list)
        mnx, mmx = math.inf, -math.inf
        mny, mmy = math.inf, -math.inf
        for (x, y) in coords:
            xes[x].append(y)
            yes[y].append(x)
            mnx = min(mnx, x)
            mny = min(mny, y)
            mmx = max(mmx, x)
            mmy = max(mmy, y)

        ans = -1
        for i in xes:
            if len(xes[i]) < 2:
                continue
            mn, mm = math.inf, -math.inf
            for y in xes[i]:
                mn = min(mn, y)
                mm = max(mm, y)
            b = mm - mn
            h0 = i - mnx
            h1 = mmx - i
            ans = max(ans, b * h0, b * h1)
        for i in yes:
            if len(yes[i]) < 2:
                continue
            mn, mm = math.inf, -math.inf
            for x in yes[i]:
                mn = min(mn, x)
                mm = max(mm, x)
            b = mm - mn
            h0 = i - mny
            h1 = mmy - i
            ans = max(ans, b * h0, b * h1)

        if ans == 0:
            return -1
        else:
            return ans
