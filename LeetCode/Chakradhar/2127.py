class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        indeg = [0 for _ in range(n)]
        pairs = set()
        for u in range(n):
            v = favorite[u]
            indeg[v] += 1
            if u == favorite[v]:
                pairs.add(u)
                pairs.add(v)

        q = deque([])
        for u in range(n):
            if indeg[u] == 0:
                q.append((u, 1))

        tail = {}
        vis = set()
        while q:
            u, l = q.popleft()
            vis.add(u)
            v = favorite[u]
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append((v, l+1))
            elif v in pairs:
                tail[v] = max(tail.get(v, 0), l)

        ans = 0
        for u in pairs:
            ans += (1 + tail.get(u, 0))

        def dfs(u, l):
            lvl[u] = l
            v = favorite[u]
            if v in lvl:
                return (l - lvl[v] + 1)
            else:
                return dfs(v, l+1)

        lvl = {}
        for u in range(n):
            if u not in vis and u not in pairs and u not in lvl:
                ans = max(ans, dfs(u, 0))

        return ans
