class TreeNode():
    def __init__(self):
        self.val = 0    # max height in this range
        self.lst = None
        self.rst = None
        self.lazy = 0   # set this range to this height

class ST():
    def __init__(self, n):
        self.n = n
        self.tree = TreeNode()

    def _merge(self, lst, rst):
        return max(lst, rst)

    def _apply(self, i, s, e):
        if i.lazy != 0:
            i.val = i.lazy
            if e - s > 1:
                if i.lst is None:
                    i.lst = TreeNode()
                    i.rst = TreeNode()
                i.lst.lazy = i.lazy
                i.rst.lazy = i.lazy
            i.lazy = 0

    def _update1(self, i, s, e, l, r, d):
        # add d to this range
        self._apply(i, s, e)
        if s >= r or l >= e:
            return
        elif l <= s and e <= r:
            i.val += d
        else:
            m = s + (e - s) // 2
            if i.lst is None:
                i.lst = TreeNode()
                i.rst = TreeNode()
            self._update1(i.lst, s, m, l, r, d)
            self._update1(i.rst, m, e, l, r, d)
            i.val = self._merge(
                i.lst.val,
                i.rst.val
            )

    def _update2(self, i, s, e, l, r, v):
        # set this range to v
        self._apply(i, s, e)
        if s >= r or l >= e:
            return
        elif l <= s and e <= r:
            i.lazy = v
            self._apply(i, s, e)
        else:
            m = s + (e - s) // 2
            self._update2(i.lst, s, m, l, r, v)
            self._update2(i.rst, m, e, l, r, v)
            i.val = self._merge(
                i.lst.val,
                i.rst.val
            )

    def update(self, l, r, d):
        # add square
        self._update1(self.tree, 0, self.n, l, r, d)
        # get max height in this range
        v = self.query(self.tree, 0, self.n, l, r)
        # set the entire range to be the max height
        self._update2(self.tree, 0, self.n, l, r, v)
        return self.tree.val    # current max height

    def query(self, i, s, e, l, r):
        if s >= r or l >= e:
            return 0
        elif l <= s and e <= r:
            return i.val
        else:
            m = s + (e - s) // 2
            if i.lst is None:
                i.lst = TreeNode()
                i.rst = TreeNode()
            return self._merge(
                self.query(i.lst, s, m, l, r),
                self.query(i.rst, m, e, l, r)
            )


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        N = 10**8 + 10**6 + 1
        st = ST(N)

        ans = []
        for l, a in positions:
            ans.append(st.update(l, l+a, a))

        return ans
