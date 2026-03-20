class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        def union(a, b):
            aRep, bRep = find(a), find(b)
            if aRep != bRep:
                par[bRep] = aRep

        def find(a):
            if par[a] != a:
                par[a] = find(par[a])
            return par[a]

        par = {}
        size = {}
        for x, y in points:
            kx = f'x{x}'
            ky = f'y{y}'
            if kx not in par:
                par[kx] = kx
                size[kx] = 0
            if ky not in par:
                par[ky] = ky
                size[ky] = 0
            size[kx] += 1
            size[ky] += 1
            union(f'x{x}', f'y{y}')

        for k in par:
            if k[0] == 'y' or par[k] == k:
                continue
            size[par[k]] += size[k]

        mx0, mx1 = 0, 0
        for k in par:
            if k[0] == 'y' or par[k] != k:
                continue
            if mx0 <= size[k]:
                mx0, mx1 = size[k], mx0
            elif mx1 <= size[k]:
                mx1 = size[k]

        return mx0 + mx1 + 1
