class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(sx, sy, dx, dy):
            vis = {(sx, sy)}
            q = deque([(sx, sy)])
            dist = 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    if (x, y) == (dx, dy):
                        return dist

                    for (i, j) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if (0 <= i < m) and (0 <= j < n) and \
                            forest[i][j] != 0 and (i, j) not in vis:
                                vis.add((i, j))
                                q.append((i, j))
                dist += 1
            return math.inf

        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], (i, j)))
        heapq.heapify(trees)

        ans = 0
        prev = (0, 0)
        while trees:
            _, cur = heapq.heappop(trees)
            ans += bfs(*prev, *cur)
            if ans == math.inf:
                return -1
            prev = cur

        return ans
