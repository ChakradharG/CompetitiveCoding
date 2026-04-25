class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = 0
        for mask in range(1, 1<<n):
            nodes = set()
            sm = 0
            for b in range(n):
                if mask>>b & 0b1:
                    nodes.add(b)
                    sm ^= nums[b]
            if sm:
                continue
            q = deque([nodes.pop()])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v in nodes:
                        nodes.remove(v)
                        q.append(v)
            if len(nodes) == 0:
                ans += 1

        return ans
