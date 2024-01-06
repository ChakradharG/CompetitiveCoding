class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        sortedStarts = [s for s, *_ in jobs]

        row = [0 for _ in range(len(profit) + 1)]
        for i in range(len(profit) - 1, -1, -1):
            row[i] = max(
                jobs[i][2] + row[bisect_left(sortedStarts, jobs[i][1], i)],
                row[i+1]
            )

        return row[0]
