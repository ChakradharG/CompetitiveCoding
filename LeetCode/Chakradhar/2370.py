class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        s = list(map(lambda x: ord(x) - 96, s))

        row = [0 for _ in range(27)]    # idx 0 -> blank

        for i in range(n-1, -1, -1):
            pivot = s[i]
            l = max(1, pivot - k)
            r = min(26, pivot + k)

            indices = set(range(l, r + 1))
            indices.add(0)
            indices.remove(pivot)

            for j in indices:   # loop over ideal indices only (and blank)
                row[j] = max(
                    row[j],         # skip
                    row[pivot] + 1  # include
                )
            row[pivot] += 1

        return max(row)
