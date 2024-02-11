class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        mat0 = [[0 for j in range(C+2)] for i in range(C+2)]
        mat1 = [[0 for j in range(C+2)] for i in range(C+2)]

        for i in range(C):
            for j in range(C):
                if i == j:
                    mat1[i+1][j+1] = grid[-1][i]
                else:
                    mat1[i+1][j+1] = grid[-1][i] + grid[-1][j]

        for k in range(R-2, -1, -1):
            for i in range(C):
                for j in range(i+1, C):
                    I, J = i+1, j+1
                    mat0[I][J] = grid[k][i] + grid[k][j] + max(
                        mat1[I-1][J-1], mat1[I-1][J], mat1[I-1][J+1],
                        mat1[I][J-1], mat1[I][J], mat1[I][J+1],
                        mat1[I+1][J-1], mat1[I+1][J], mat1[I+1][J+1]
                    )
            mat0, mat1 = mat1, mat0

        return mat1[1][-2]
