class Solution:
    def costWithEdgeLimit(self, limit: int) -> int:
        # cost from 0 -> n-1 while only picking edges with cost >= limit
        dist = [inf for _ in range(self.n)]
        dist[0] = 0
        q = deque([(0, 0)])
        while q:
            u, d = q.popleft()
            if d > dist[u]:
                continue
            for v, cost in self.graph[u]:
                if cost < limit or (nd := d+cost) >= dist[v]:
                    continue
                dist[v] = nd
                q.append((v, nd))

        return dist[self.n-1]

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        self.n = len(online)
        self.graph = [[] for _ in range(self.n)]
        costs = set()
        for u, v, cost in edges:
            if not (online[u] and online[v]):
                # remove offline nodes from the graph entirely
                continue
            self.graph[u].append((v, cost))
            costs.add(cost)
        costs = sorted(costs)

        l, r = 0, len(costs)-1
        while l <= r:
            m = l + (r - l) // 2
            if self.costWithEdgeLimit(costs[m]) <= k:
                l = m + 1
            else:
                r = m - 1

        if r == -1:
            return -1
        else:
            return costs[r]
