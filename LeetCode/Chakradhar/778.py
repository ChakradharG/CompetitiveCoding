class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        vis, n = {(0, 0)}, len(grid)
        heap = [(grid[0][0], 0, 0)]
        d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        while heap:
            t, i, j = heapq.heappop(heap)

            if i == n-1 and j == n-1:
                return t
            for di, dj in d:
                ni, nj = i + di, j + dj
                if (not (0 <= ni < n and 0 <= nj < n)) or (ni, nj) in vis:
                    continue
                vis.add((ni, nj))
                heapq.heappush(heap, (max(t, grid[ni][nj]), ni, nj))
