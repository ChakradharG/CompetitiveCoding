class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        par = list(range(n))
        cost = [None for _ in range(n)]

        def union(a, b, cs):
            aRep, bRep = find(a), find(b)
            par[bRep] = aRep
            if cost[aRep] is None:
                cost[aRep] = cs
            else:
                cost[aRep] &= cs
            if cost[bRep] is not None:
                cost[aRep] &= (cost[bRep] & cs)

        def find(a):
            if par[a] != a:
                par[a] = find(par[a])
            return par[a]

        for u, v, w in edges:
            union(u, v, w)

        ans = []
        for s, t in query:
            s, t = find(s), find(t)
            if s != t:
                ans.append(-1)
            else:
                ans.append(cost[s])

        return ans
