class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        q = []

        nextInRow = [{} for i in range(m)]
        for i in range(m):
            temp = set()
            for j in range(n):
                temp.add(mat[i][j])
                q.append((i, j))
            temp = sorted(list(temp))
            for l in range(len(temp)-1):
                nextInRow[i][temp[l]] = temp[l+1]
            nextInRow[i][temp[-1]] = math.inf

        q.sort(key= lambda x: mat[x[0]][x[1]])

        nextInCol = [{} for j in range(n)]
        for j in range(n):
            temp = set()
            for i in range(m):
                temp.add(mat[i][j])
            temp = sorted(list(temp))
            for l in range(len(temp)-1):
                nextInCol[j][temp[l]] = temp[l+1]
            nextInCol[j][temp[-1]] = math.inf

        valInRow = [{} for i in range(m)]
        valInCol = [{} for j in range(n)]
        ans = 1
        for (i, j) in q:
            v = mat[i][j]
            x = max(valInRow[i].get(v, 1), valInCol[j].get(v, 1))
            nr = nextInRow[i][v]
            valInRow[i][nr] = max(valInRow[i].get(nr, 1), x+1)
            nc = nextInCol[j][v]
            valInCol[j][nc] = max(valInCol[j].get(nc, 1), x+1)
            ans = max(ans, x)

        return ans
