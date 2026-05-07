class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        m, n = len(robots), len(walls)
        walls.sort()
        bullets = list(sorted(zip(robots, distance)))

        r_wall_cnt = [0 for _ in range(m)] # number of walls that can be destroyed to the right
        l_wall_cnt = [0 for _ in range(m)] # number of walls that can be destroyed to the left
        l_wall_cnt2 = [0 for _ in range(m)] # number of walls that can be destroyed to the left given prev robot shoots right
        pp = None
        for i, (p, dist) in enumerate(bullets):
            p0r = bisect_left(walls, p)
            r = p + dist
            if i < m-1:
                r = min(r, bullets[i+1][0]-1)
            pr = bisect_right(walls, r)
            r_wall_cnt[i] = pr - p0r
            p0l = bisect_right(walls, p)
            l = p - dist
            if i > 0:
                l = max(l, bullets[i-1][0]+1)
            pl = bisect_left(walls, l)
            l_wall_cnt[i] = p0l - pl
            if i == 0:
                l_wall_cnt2[i] = l_wall_cnt[i]
            else:
                l_wall_cnt2[i] = l_wall_cnt[i] - max(0, pp - pl)
            pp = pr

        @cache
        def dfs(i, prev_r):
            if i == m:
                return 0
            res = r_wall_cnt[i] + dfs(i+1, True)
            if prev_r:
                res = max(res, l_wall_cnt2[i] + dfs(i+1, False))
            else:
                res = max(res, l_wall_cnt[i] + dfs(i+1, False))
            return res

        return dfs(0, False)
