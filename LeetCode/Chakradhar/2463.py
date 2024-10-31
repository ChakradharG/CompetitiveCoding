class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory = list(sorted(filter(lambda f: f[1] != 0, factory))) + [[math.inf, 1]]
        m, n = len(robot), len(factory)-1

        def dfs(i, j, l):
            if i == m:
                return 0
            if j == n:
                return math.inf
            key = (i, j, l)
            if key not in memo:
                memo[key] = dfs(i, j+1, factory[j+1][1])
                if l != 0:
                    memo[key] = min(
                        memo[key],
                        abs(robot[i] - factory[j][0]) + dfs(i+1, j, l-1)
                    )
            return memo[key]

        memo = {}
        dfs(0, 0, factory[0][1])
        return dfs(0, 0, factory[0][1])
