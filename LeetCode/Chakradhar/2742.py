class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        row0 = [0 for _ in range(n+1)]
        row1 = [math.inf for _ in range(n+1)]
        row1[-1] = 0

        for i in reversed(range(n)):
            for done in range(n):
                row0[done] = min(
                    row1[done], # skip this
                    cost[i] + row1[min(n, done + time[i] + 1)]  # paint this
                    # free painter picks up `time[i]` walls while paid painter is busy with this
                )
            row0, row1 = row1, row0

        return row1[0]
