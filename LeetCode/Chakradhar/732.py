class TreeNode:
    def __init__(self):
        self.val = 0
        self.lst = None
        self.rst = None
        self.lazy = 0

class ST:
    def __init__(self):
        self.tree = TreeNode() # root node

    def _merge(self, lst, rst):
        return max(lst, rst)

    def _create(self, i):
        if i.lst is None:
            i.lst = TreeNode()
            i.rst = TreeNode()

    def _apply(self, i, s, e):
        if i.lazy != 0:
            i.val += i.lazy
            if e - s > 1:
                self._create(i) # only create nodes when required
                i.lst.lazy += i.lazy
                i.rst.lazy += i.lazy
            i.lazy = 0

    def update(self, i, s, e, l, r, d):
        # d = new val - old val, i.e., the delta and not new val
        self._apply(i, s, e)
        if s >= r or e <= l:
            pass
        elif l <= s and e <= r:
            i.lazy = d
            self._apply(i, s, e)
        else:
            m = s + (e - s) // 2
            self._create(i) 
            i.val = self._merge(
                self.update(i.lst, s, m, l, r, d),
                self.update(i.rst, m, e, l, r, d)
            )
        return i.val


class MyCalendarThree:

    def __init__(self):
        self.n = 10**9 + 1
        self.st = ST()

    def book(self, startTime: int, endTime: int) -> int:
        self.st.update(self.st.tree, 0, self.n, startTime, endTime, +1)
        return self.st.tree.val


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)

