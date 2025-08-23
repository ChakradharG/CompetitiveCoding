class TreeNode():
    def __init__(self):
        self.val = 0 # range sum
        self.lst = None
        self.rst = None
        self.lazy = 0

class ST():
    def __init__(self):
        self.tree = TreeNode() # root node

    def _merge(self, lst, rst):
        return lst + rst

    def _create(self, i):
        if i.lst is None:
            i.lst = TreeNode()
            i.rst = TreeNode()

    def _apply(self, i, s, e):
        if i.lazy != 0:
            i.val = (e - s) * i.lazy
            if e - s > 1:
                self._create(i)
                i.lst.lazy = i.lazy
                i.rst.lazy = i.lazy
            i.lazy = 0

    def update(self, i, s, e, l, r):
        self._apply(i, s, e)
        if s >= r or e <= l:
            return
        elif l <= s and e <= r:
            i.lazy = 1
            self._apply(i, s, e)
        else:
            m = s + (e - s) // 2
            self._create(i) 
            self.update(i.lst, s, m, l, r)
            self.update(i.rst, m, e, l, r)
            i.val = self._merge(
                i.lst.val,
                i.rst.val
            )


class CountIntervals:

    def __init__(self):
        self.n = 10**9 + 1
        self.st = ST()

    def add(self, left: int, right: int) -> None:
        self.st.update(self.st.tree, 0, self.n, left, right+1)

    def count(self) -> int:
        return self.st.tree.val


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()