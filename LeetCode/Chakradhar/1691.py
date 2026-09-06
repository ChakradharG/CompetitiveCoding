class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for i in range(n):
            cuboids[i].sort(reverse=True)
        cuboids.sort(reverse=True)

        row0 = [0] * (n + 1)
        row1 = [0] * (n + 1)

        for i in reversed(range(n)):
            row0[-1] = max(row1[-1], cuboids[i][0] + row1[i])
            for j in range(i):
                row0[j] = row1[j] # skip
                if (cuboids[i][0] <= cuboids[j][0]) and \
                    (cuboids[i][1] <= cuboids[j][1]) and \
                    (cuboids[i][2] <= cuboids[j][2]):
                    row0[j] = max(row0[j], cuboids[i][0] + row1[i])
            row0, row1 = row1, row0

        return row1[-1]

