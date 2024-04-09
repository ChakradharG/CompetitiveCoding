class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)
        def union(a, b, par):
            aRep, bRep = find(a, par), find(b, par)
            par[bRep] = aRep
            return aRep == bRep

        def find(a, par):
            if par[a] != a:
                par[a] = find(par[a], par)
            return par[a]

        par1 = list(range(n + 1))
        par2 = list(range(n + 1))

        cnt = 0
        cmp1, cmp2 = n, n
        for (t, u, v) in edges:
            if t == 1:
                if union(u, v, par1):
                    cnt += 1
                else:
                    cmp1 -= 1
            elif t == 2:
                if union(u, v, par2):
                    cnt += 1
                else:
                    cmp2 -= 1
            else:
                d1 = union(u, v, par1)
                d2 = union(u, v, par2)
                if d1 and d2:
                    cnt += 1
                if not d1:
                    cmp1 -= 1
                if not d2:
                    cmp2 -= 1

        if cmp1 != 1 or cmp2 != 1:
            return -1
        return cnt
