class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = {(i+1): [] for i in range(n)}
        for (u, v) in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(0, 1)])
        seen = {(i+1): [] for i in range(n)}    # for 2nd min time, any node will only be visited at most twice
        while q:
            t, u = q.popleft()
            # `t` is the time taken to reach `u`
            if (t // change) % 2:
                t = change * (1 + (t // change))
            # now `t` also includes stopping at `u` for red signal
            for v in adj[u]:
                w = t + time   # to traverse the edge
                if (len(seen[v]) == 0) or \
                   (len(seen[v]) == 1 and seen[v][0] != w):
                   # haven't been visited previously
                   # or visited but the time taken is different than current time
                   # (because if the time taken to reach `n` using different paths is
                   # [10, 10, 12], we have to return 12 and not 10)
                    seen[v].append(w)
                    q.append((w, v))
                if v == n and len(seen[v]) == 2:    # second time visiting `n`
                    return w
