class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        factories = []
        for (p, l) in factory:
            factories.extend([p]*l)
        m, n = len(robot), len(factories)

        row0 = [0 for _ in range(n+1)]
        row1 = [0 for _ in range(n+1)]

        for i in reversed(range(m)):
            row0[-1] = math.inf
            for j in reversed(range(n)):
                row0[j] = min(row0[j+1], abs(robot[i] - factories[j]) + row1[j+1])
            row0, row1 = row1, row0

        return row1[0]
