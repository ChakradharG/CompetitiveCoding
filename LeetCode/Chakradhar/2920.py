class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        if k == 0:
            return sum(coins)

        def calcMax(node):
            vis.add(node)
            for child in adj[node]:
                if child not in vis:
                    maxInSub[node] = max(
                        maxInSub[node],
                        calcMax(child)
                    )
            vis.remove(node)
            return maxInSub[node]

        def dfs(node, red):
            if red > maxInSub[node]:
                return 0
            key = (node, red)
            if key not in memo:
                vis.add(node)
                res = [0, 0]
                for child in adj[node]:
                    if child not in vis:
                        res[0] += dfs(child, red)
                        res[1] += dfs(child, red*2)
                memo[key] = max(
                    res[0] + (coins[node]//red - k),
                    res[1] + (coins[node]//(red*2))
                )
                vis.remove(node)
            return memo[key]

        n = len(coins)
        adj = {i: [] for i in range(n)}
        for (u, v) in edges:
            adj[u].append(v)
            adj[v].append(u)

        maxInSub = coins.copy()
        vis = set()
        calcMax(0)

        memo = {}
        return dfs(0, 1)
