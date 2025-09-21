class ST:
    def __init__(self, a, mx):
        self.a = a
        self.max = mx
        self.tree = [0 for _ in range(4*len(a))]
        self._build(0, 0, len(a))

    def _build(self, i, s, e):
        if e - s == 1:
            self.tree[i] = self.a[s]
        else:
            m = s + (e - s) // 2
            self._build(2*i+1, s, m)
            self._build(2*i+2, m, e)
            self.tree[i] = self._merge(
                self.tree[2*i+1],
                self.tree[2*i+2]
            )

    def _merge(self, lst, rst):
        if self.max:
            return max(lst, rst)
        else:
            return min(lst, rst)

    def query(self, i, s, e, l, r):
        if s >= r or l >= e:
            if self.max:
                return -math.inf
            else:
                return math.inf
        elif l <= s and e <= r:
            return self.tree[i]
        else:
            m = s + (e - s) // 2
            return self._merge(
                self.query(2*i+1, s, m, l, r),
                self.query(2*i+2, m, e, l, r)
            )


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mn = ST(nums, False)
        mx = ST(nums, True)

        @cache
        def getVal(l, r):
            return mn.query(0, 0, n, l, r) - mx.query(0, 0, n, l, r)

        h = [(getVal(0, n), 0, n)]
        ans = 0
        enqd = {(0, n)}
        while k:
            x, l, r = heappop(h)
            ans -= x
            if r - l > 1:
                if (l, r-1) not in enqd:
                    heappush(h, (getVal(l, r-1), l, r-1))
                    enqd.add((l, r-1))
                if (l+1, r) not in enqd:
                    heappush(h, (getVal(l+1, r), l+1, r))
                    enqd.add((l+1, r))
            k -= 1

        return ans
