class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(
            [(s, e, p) for (s, e, p) in zip(startTime, endTime, profit)]
        )
        sortedStarts = [s for s, *_ in jobs]
        next_non_overlap = [
            bisect.bisect_left(sortedStarts, jobs[i][1], i)
            for i in range(len(jobs))
        ]

        row = [0 for _ in range(len(profit)+1)]
        for i in range(len(profit)-1, -1, -1):
            row[i] = max(
                jobs[i][2] + row[next_non_overlap[i]],
                row[i+1]
            )

        return row[0]
