class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        rests = sorted(
            [[0, 0], [n-1, n-1]] + 
            [[i-1, h] for (i, h) in restrictions]
        )   # adding default cases to rests and sorting by id

        # 1st pass (l to r)
        for i in range(1, len(rests)):
            diff = rests[i][0] - rests[i-1][0]
            rests[i][1] = min(
                rests[i-1][1] + diff,
                rests[i][1]
            )

        ans = rests[-1][1]
        # 2nd pass (r to l)
        for i in range(len(rests)-2, -1, -1):
            diff = rests[i+1][0] - rests[i][0]
            rests[i][1] = min(
                rests[i+1][1] + diff,
                rests[i][1]
            )
            hdiff = abs(rests[i+1][1] - rests[i][1])
            if (diff - hdiff) > 1:
                # mountain b/w i and i+1 (i.e., peak somewhere in between)
                d = (diff - hdiff) // 2
                peak = max(rests[i][1], rests[i+1][1]) + d
                ans = max(ans, peak)
            else:
                ans = max(ans, rests[i][1])

        return ans
