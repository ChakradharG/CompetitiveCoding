class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append([v, t])

        dist = [[inf for p in range(power+1)] for _ in range(n)]
        dist[source][power] = 0
        h = [(0, -power, source)]
        while h:
            t, p, u = heappop(h)
            p *= -1
            if t > dist[u][p]:
                continue
            if u == target:
                return [t, p]
            p -= cost[u]
            if p < 0:
                continue
            for v, dt in graph[u]:
                nt = t + dt
                if nt < dist[v][p]:
                    dist[v][p] = nt
                    heappush(h, (nt, -p, v))

        return [-1, -1]

