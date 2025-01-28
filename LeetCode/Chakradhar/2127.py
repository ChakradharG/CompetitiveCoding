class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        def maxTail(u):
            vis.add(u)
            tail = 0
            for v in rev[u]:
                if v not in vis:
                    tail = max(tail, maxTail(v))
            return tail + 1

        n = len(favorite)
        rev = [[] for _ in range(n)]    # reverse nodes
        for u in range(n):
            v = favorite[u]
            if u != favorite[v]:
                rev[favorite[u]].append(u)

        vis, ans = set(), 0
        for u in range(n):
            v = favorite[u]
            if u == favorite[v]:
                ans += maxTail(u)

        # find length of cycles
        def dfs(u, l):
            vis.add(u)
            lvl[u] = l
            v = favorite[u]
            if lvl.get(v, -1) != -1:
                x = (l - lvl[v] + 1)
            else:
                x = dfs(v, l+1)
            lvl[u] = -1
            return x

        lvl = {}
        for u in range(n):
            if u not in vis:
                ans = max(ans, dfs(u, 0))
                print(u, ans)

        return ans
