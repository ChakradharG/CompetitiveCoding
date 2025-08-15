class ST:
    def __init__(self):
        self.tree = defaultdict(bool)   # is all of this range being tracked
        self.lazy = defaultdict(int)

    def _merge(self, lst, rst):
        return lst and rst

    def _apply(self, i, s, e):
        if self.lazy[i] != 0:
            if self.lazy[i] == 1:
                self.tree[i] = True
            else:
                self.tree[i] = False
            if e - s > 1:
                self.lazy[2*i+1] = self.lazy[i]
                self.lazy[2*i+2] = self.lazy[i]
            self.lazy[i] = 0

    def query(self, i, s, e, l, r):
        self._apply(i, s, e)
        if s >= r or e <= l:
            return True
        elif l <= s and e <= r:
            return self.tree[i]
        else:
            m = s + (e - s) // 2
            return self._merge(
                self.query(2*i+1, s, m, l, r),
                self.query(2*i+2, m, e, l, r)
            )

    def update(self, i, s, e, l, r, d):
        self._apply(i, s, e)
        if s >= r or e <= l:
            return
        elif l <= s and e <= r:
            self.lazy[i] = d
            self._apply(i, s, e)
        else:
            m = s + (e - s) // 2
            self.update(2*i+1, s, m, l, r, d)
            self.update(2*i+2, m, e, l, r, d)
            self.tree[i] = self._merge(
                self.tree[2*i+1],
                self.tree[2*i+2]
            )


class RangeModule:

    def __init__(self):
        self.N = 10**9 + 1
        self.st = ST()

    def addRange(self, left: int, right: int) -> None:
        self.st.update(0, 0, self.N, left, right, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.st.query(0, 0, self.N, left, right)

    def removeRange(self, left: int, right: int) -> None:
        self.st.update(0, 0, self.N, left, right, -1)
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)