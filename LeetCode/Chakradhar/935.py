import numpy as np

class Solution:
    def knightDialer(self, n: int) -> int:
        v = np.array([[1, 1, 1, 1]])    # 1 x 4
        A = np.matrix([
            [0, 0, 0, 1],
            [0, 0, 2, 2],
            [0, 1, 0, 0],
            [2, 1, 0, 0]
        ], dtype=object)  # np.MATRIX, not np.ndarray. A**2 => A @ A
        # dtype=object to avoid overflow

        res = v @ (A ** (n-1))
        cnt = (np.asarray(res) * np.array([[1, 4, 2, 2]])).sum()

        if n == 1:
            cnt += 1
        return cnt % (10**9 + 7)
