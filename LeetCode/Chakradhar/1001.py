class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def neighbors(i, j):
            nei = []
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni = i + di
                    nj = j + dj
                    if (0 <= ni < n) and (0 <= nj < n):
                        nei.append((ni, nj))
            return nei

        def isIlluminated(i, j):
            return int(
                (rows[i] > 0) or
                (cols[j] > 0) or
                (dia1[i-j] > 0) or 
                (dia2[i+j] > 0)
            )

        def turnOn(i, j):
            rows[i] += 1
            cols[j] += 1
            dia1[i-j] += 1
            dia2[i+j] += 1

        def turnOff(i, j):
            rows[i] -= 1
            cols[j] -= 1
            dia1[i-j] -= 1
            dia2[i+j] -= 1

        lamps = {*map(tuple, lamps)}    # remove duplicate lamps
        rows = defaultdict(int)
        cols = defaultdict(int)
        dia1 = defaultdict(int) # i - j = constant
        dia2 = defaultdict(int) # i + j = constant

        for (i, j) in lamps:
            turnOn(i, j)

        ans = []
        for (i, j) in queries:
            ans.append(isIlluminated(i, j))
            for (ni, nj) in neighbors(i, j):
                if (ni, nj) in lamps:
                    turnOff(ni, nj)
                    lamps.remove((ni, nj))

        return ans
