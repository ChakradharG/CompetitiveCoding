class Solution:
    def latestDayToCross(
        self, row: int, col: int, cells: List[List[int]]
    ) -> int:
        def union(x, y):
            repX, repY = find(x), find(y)
            if repX[0] != repY[0]:
                if (repY[0][0] < repX[0][0]) or \
                (repY[0][0] == repX[0][0] and repY[0][1] < repX[0][1]):
                    repX, repY = repY, repX
                rep[repY[0]][0] = repX[0]
                repX[2] = max(repX[2], repY[2])
            return repX[2] - repX[1] + 1

        def find(x):
            if rep[x][0] != x:
                rep[x] = find(rep[x][0])
            return rep[x]

        rep = {(r, c): [(r,c), r, r] for c in range(col) for r in range(row)}
        land = set()

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            land.add((r, c))
            if (r, c - 1) in land:
                if union((r, c - 1), (r, c)) == row:
                    return i
            if (r, c + 1) in land:
                if union((r, c), (r, c + 1)) == row:
                    return i
            if (r - 1, c) in land:
                if union((r - 1, c), (r, c)) == row:
                    return i
            if (r + 1, c) in land:
                if union((r, c), (r + 1, c)) == row:
                    return i
