class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)

        row = [0 for _ in range(26)]

        for i in range(n-1, -1, -1):
            pivot = ord(s[i]) - 97
            l = max(0, pivot - k)
            r = min(25, pivot + k)

            indices = set(range(l, r + 1))
            indices.remove(pivot)

            for j in indices:   # loop over ideal indices only
                row[j] = max(
                    row[j],         # skip
                    row[pivot] + 1  # include
                )
            row[pivot] += 1

        return max(row)
