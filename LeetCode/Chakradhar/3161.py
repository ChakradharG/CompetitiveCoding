from dataclasses import dataclass

@dataclass
class TreeNode:
    mxL: int
    mxR: int
    mx: int
    isCont: bool

class ST:
    def __init__(self, n):
        self.tree = [TreeNode(1, 1, 1, True) for _ in range(4*n)]
        self._build(0, 0, n)
    def _build(self, i, s, e):
        if e - s > 1:
            m = s + (e - s) // 2
            self._build(2*i+1, s, m)
            self._build(2*i+2, m, e)
            self.tree[i] = self._merge(
                self.tree[2*i+1],
                self.tree[2*i+2]
            )
    def _merge(self, lst, rst):
        mxL = (lst.mx + rst.mxL) if lst.isCont else lst.mxL
        mxR = (lst.mxR + rst.mx) if rst.isCont else rst.mxR
        return TreeNode(
            mxL,
            mxR,
            max(
                lst.mxR + rst.mxL,
                mxL, mxR,
                lst.mx, rst.mx
            ),
            lst.isCont and rst.isCont
        )
    def query(self, i, s, e, x):
        if s >= x:
            return TreeNode(0, 0, 0, False)
        elif e <= x:
            return self.tree[i]
        else:
            m = s + (e - s) // 2
            return self._merge(
                self.query(2*i+1, s, m, x),
                self.query(2*i+2, m, e, x)
            )
    def update(self, i, s, e, x):
        if s > x or e < x:
            return
        if e - s == 1:
            self.tree[i].isCont = False
            if s == x:
                self.tree[i].mxL = 0
            else:
                self.tree[i].mxR = 0
        else:
            m = s + (e - s) // 2
            self.update(2*i+1, s, m, x)
            self.update(2*i+2, m, e, x)
            self.tree[i] = self._merge(
                self.tree[2*i+1],
                self.tree[2*i+2]
            )

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = min(5 * 10**4, 3 * len(queries))
        st = ST(n)
        results = []
        for t, *p in queries:
            if t == 1:
                st.update(0, 0, n, p[0])
            else:
                results.append(st.query(0, 0, n, p[0]).mx >= p[1])

        return results
