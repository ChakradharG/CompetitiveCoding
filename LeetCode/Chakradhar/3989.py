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

        d = 0
        while q:
            levelQd = set()
            for _ in range(len(q)):
                a = q.popleft()
                for b in graph[a]:
                    if b not in levelQd:
                        q.append(b)
                        levelQd.add(b)
            d += 1

        return d
