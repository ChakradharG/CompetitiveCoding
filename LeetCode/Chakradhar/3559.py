class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        MOD = 10**9 + 7

        down = defaultdict(set)
        up = {}
        depth = {}
        for u, v in edges:
            down[u].add(v)
            down[v].add(u)

        q = deque([1])
        d = 0
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                depth[u] = d
                for v in down[u]:
                    down[v].remove(u)
                    up[v] = u
                    q.append(v)
            d += 1

        def count(u, v):
            if depth[u] > depth[v]:
                return count(v, u)
            dist = 0
            while depth[v] != depth[u]:
                v = up[v]
                dist += 1
            while u != v:
                u = up[u]
                v = up[v]
                dist += 2
            return dfs(dist, 0)

        memo = {}
        def dfs(rem, parity):
            if rem == 0:
                return parity
            key = (rem, parity)
            if key not in memo:
                memo[key] = (
                    dfs(rem-1, parity) + 
                    dfs(rem-1, not parity)
                ) % MOD
            return memo[key]

        ans = []
        for u, v in queries:
            ans.append(count(u, v))
        return ans

