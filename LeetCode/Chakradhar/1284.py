class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        ops = [
            [0b110100000, 0b111010000, 0b011001000],
            [0b100110100, 0b010111010, 0b001011001],
            [0b000100110, 0b000010111, 0b000001011]
        ]
        m, n = len(mat), len(mat[0])
        st, mask = 0, 0
        for i in range(3):
            for j in range(3):
                st <<= 1
                mask <<= 1
                if i < m and j < n:
                    st += mat[i][j]
                    mask += 1

        q = deque([st])
        enqd = {st}
        d = 0
        while q:
            for _ in range(len(q)):
                t = q.popleft()
                if t == 0:
                    return d
                for i in range(m):
                    for j in range(n):
                        x = (t ^ ops[i][j]) & mask
                        if x not in enqd:
                            enqd.add(x)
                            q.append(x)
            d += 1

        return -1

