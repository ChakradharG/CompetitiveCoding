class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
        adj = [[] for _ in range(n)]
        weights = {0}
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            weights.add(w)
        weights = sorted(weights)

        vis = set()
        l, r = 0, len(weights)-1
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            thresh = weights[m]

            # BFS
            dist = [math.inf for _ in range(n)]
            dist[source] = 0
            q = deque([source])
            while q:
                u = q.popleft()
                for v, w in adj[u]:
                    cost = 0 if w <= thresh else 1
                    if dist[v] > dist[u] + cost:
                        dist[v] = dist[u] + cost
                        if cost == 0:
                            q.appendleft(v)
                        else:
                            q.append(v)

            if dist[target] <= k:
                res = thresh
                r = m - 1
            else:
                l = m + 1

        return res
