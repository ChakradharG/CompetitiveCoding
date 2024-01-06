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

        def dfs(idx, lastEnd):
            if idx == len(startTime):
                return 0

            if idx not in memo:
                memo[idx] = max(
                    jobs[idx][2] + dfs(next_non_overlap[idx], jobs[idx][1]),
                    dfs(idx+1, lastEnd)
                )

            return memo[idx]

        memo = {}
        return dfs(0, 0)
