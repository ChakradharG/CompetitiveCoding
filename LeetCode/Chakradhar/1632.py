class TwoDGrid:
    def __init__(self, m: int, n: int, f: Callable[[int, int], int]) -> None:
        self.grid = [[f(i, j) for j in range(n)] for i in range(m)]

    def __getitem__(self, idx: tuple[int, int]) -> tuple[int, int]:
        return self.grid[idx[0]][idx[1]]

    def __setitem__(self, idx: tuple[int, int], val: int) -> None:
        self.grid[idx[0]][idx[1]] = val


class DSU:
    def __init__(self, m: int, n: int) -> None:
        self.par = TwoDGrid(m, n, lambda i, j: (i, j))
        self.val = TwoDGrid(m, n, lambda i, j: 1)

    def union(self, a: tuple[int, int], b: tuple[int, int]) -> None:
        aRep, bRep = self.find(a), self.find(b)
        self.par[bRep] = aRep

    def find(self, a: tuple[int, int]) -> tuple[int]:
        if self.par[a] != a:
            self.par[a] = self.find(self.par[a])
        return self.par[a]


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        # Union-find for equal values on same row/col
        dsu = DSU(m, n)
        h = []
        for i in range(m):
            d = {}
            for j in range(n):
                v = matrix[i][j]
                if v not in d:
                    d[v] = (i, j)
                else:
                    dsu.union(d[v], (i, j))
                h.append((matrix[i][j], i, j))
        for j in range(n):
            d = {}
            for i in range(m):
                v = matrix[i][j]
                if v not in d:
                    d[v] = (i, j)
                else:
                    dsu.union(d[v], (i, j))

        rowRank = [None] * m # [set-by-col]
        colRank = [None] * n # [set-by-row]

        for v, i, j in sorted(h):
            pj = rowRank[i] if rowRank[i] is not None else j
            pi = colRank[j] if colRank[j] is not None else i
            row = dsu.val[dsu.find((i, pj))] + (0 if (v == matrix[i][pj]) else 1)
            col = dsu.val[dsu.find((pi, j))] + (0 if (v == matrix[pi][j]) else 1)
            rep = dsu.find((i, j))
            x = max(row, col, dsu.val[rep])
            rowRank[i] = j
            colRank[j] = i
            dsu.val[rep] = x

        return [[dsu.val[dsu.find((i, j))] for j in range(n)] for i in range(m)]

