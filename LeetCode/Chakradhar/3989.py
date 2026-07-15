class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m, n = len(grid), len(grid[0])
        graph = [set(range(a+1, n)) for a in range(n)]
        indeg = list(range(n))
        q = deque([0])
        for row in grid:
            for a in range(n):
                rem = []
                for b in graph[a]:
                    if abs(row[a] - row[b]) > limit:
                        rem.append(b)
                for b in rem:
                    graph[a].remove(b)
                    indeg[b] -= 1
                    if indeg[b] == 0:
                        q.append(b)

        ans = 1
        row = [1 for _ in range(n)]
        for a in reversed(range(n-1)):
            for b in graph[a]:
                row[a] = max(row[a], row[b] + 1)
            ans = max(ans, row[a])

        return ans

