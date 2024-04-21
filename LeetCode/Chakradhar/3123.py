class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(n)}
        for i, (u, v, w) in enumerate(edges):
            adj[u].append((v, w, i))
            adj[v].append((u, w, i))

        dist = [math.inf for _ in range(n)]
        dist[0] = 0
        h = [(0, 0)]
        while h:
            w, u = heapq.heappop(h)
            if u == n - 1:
                break
            if w > dist[u]:
                continue
            for (v, w2, _) in adj[u]:
                if w + w2 < dist[v]:
                    dist[v] = w + w2
                    heapq.heappush(h, (dist[v], v))

        vis = set()
        def dfs(node, rem):
            if rem < 0:
                return False
            if node == n - 1:
                return True
            if rem == 0:
                return False

            key = (node, rem)
            if key not in memo:
                memo[key] = False
                vis.add(node)
                for (v, w, i) in adj[node]:
                    if v not in vis and dfs(v, rem-w):
                        memo[key] = True
                        ans[i] = True
                vis.remove(node)
            return memo[key]

        memo = {}
        ans = [False for _ in range(len(edges))]
        dfs(0, dist[n-1])
        return ans
