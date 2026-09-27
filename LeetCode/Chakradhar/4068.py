class BIT:
    def __init__(self, n):
        self.tree = [-inf] * n

    def query(self, i):
        res = -inf
        while i > 0:
            res = max(res, self.tree[i])
            i -= (i & -i)
        return res

    def update(self, i, d):
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], d)
            i += (i & -i)


class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings = sorted(meetings)
        unq = set()
        for l, r, w in meetings:
            unq.add(l)
            unq.add(r)
        ix = {k: i+1 for i, k in enumerate(sorted(unq))}

        bit = BIT(len(unq)+1)
        ans = 0

        for l, r, w in meetings:
            x = bit.query(ix[l])
            if x == -inf:
                y = w
            else:
                y = w + l + x
            ans = max(ans, y)
            bit.update(ix[r], y - r)

        return ans

