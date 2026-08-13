class ST:
    def __init__(self, a):
        self.a = a
        n = len(a)
        self.tree = [[0, '', 0, '', 0, 0] for _ in range(4*n)]
        self._build(0, 0, n)

    def _merge(self, lst, rst):
        if lst[5] == 0:
            x = rst
        elif rst[5] == 0:
            x = lst
        else:
            x = [lst[0], lst[1], 0, rst[3], rst[4], lst[5]+rst[5]]
            if lst[2] == lst[5] and lst[3] == rst[1]:
                x[0] += rst[0]
            if rst[2] == rst[5] and rst[1] == lst[3]:
                x[4] += lst[4]
            x[2] = max(
                lst[2], rst[2],
                x[0], x[4]
            )
            if lst[3] == rst[1]:
                x[2] = max(x[2], lst[4] + rst[0])
        return x

    def _build(self, i, s, e):
        if e - s == 1:
            self.tree[i] = [1, self.a[s], 1, self.a[s], 1, 1]
        else:
            m = s + (e - s) // 2
            self.tree[i] = self._merge(
                self._build(2*i+1, s, m),
                self._build(2*i+2, m, e)
            )
        return self.tree[i]

    def update(self, i, s, e, l, d):
        if s > l or e <= l:
            return
        elif e - s == 1 and s == l:
            self.tree[i][1] = d
            self.tree[i][3] = d
        else:
            m = s + (e - s) // 2
            self.update(2*i+1, s, m, l, d)
            self.update(2*i+2, m, e, l, d)
            self.tree[i] = self._merge(
                self.tree[2*i+1],
                self.tree[2*i+2]
            )


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = ST(s)
        n = len(s)

        ans = []
        for i, c in zip(queryIndices, queryCharacters):
            st.update(0, 0, n, i, c)
            ans.append(st.tree[0][2])

        return ans

