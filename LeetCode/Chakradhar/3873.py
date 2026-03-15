class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        def union(a, b):
            aRep, bRep = find(a), find(b)
            if aRep != bRep:
                par[bRep] = aRep
                size[aRep] += size[bRep] - 1

        def find(a):
            if par[a] != a:
                par[a] = find(par[a])
            return par[a]

        Xs = defaultdict(int)
        Ys = defaultdict(int)
        for x, y in points:
            Xs[x] += 1
            Ys[y] += 1

        par = {}
        size = {}
        for x, s in Xs.items():
            k = f'x{x}'
            par[k] = k
            size[k] = s
        for y, s in Ys.items():
            k = f'y{y}'
            par[k] = k
            size[k] = s

        for x, y in points:
            union(f'x{x}', f'y{y}')

        mx0, mx1 = 0, 0
        for x in Xs:
            k = f'x{x}'
            if par[k] != k:
                continue
            if mx0 <= size[k]:
                mx0, mx1 = size[k], mx0
            elif mx1 <= size[k]:
                mx1 = size[k]

        return mx0 + mx1 + 1
