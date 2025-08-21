class ST():
    def __init__(self, a):
        self.a = a
        n = len(a)
        self.tree = [0 for _ in range(4*n)]
        self._build(0, 0, n)

    def _merge(self, lst, rst):
        return lst | rst

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

    def query(self, i, s, e, l, r):
        if s >= r or l >= e:
            return 0
        elif l <= s and e <= r:
            return self.tree[i]
        else:
            m = s + (e - s) // 2
            return self._merge(
                self.query(2*i+1, s, m, l, r),
                self.query(2*i+2, m, e, l, r)
            )


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = ST(nums)

        l, r = 0, 0
        ans = math.inf
        x = 0
        while r < n and x <= k:
            x |= nums[r]
            ans = min(ans, abs(k - x))
            r += 1

        while l < n:
            if r == l:
                r += 1
            x = st.query(0, 0, n, l, r)
            ans = min(ans, abs(k - x))
            while r < n and x <= k:
                x |= nums[r]
                ans = min(ans, abs(k - x))
                r += 1
            l += 1

        return ans
