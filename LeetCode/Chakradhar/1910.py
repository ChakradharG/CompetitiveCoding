class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m, n = len(s), len(part)

        LPS = [0]
        p, c = 0, 1
        while c < n:
            if part[p] == part[c]:
                LPS.append(p + 1)
                p, c = p + 1, c + 1
            else:
                if p == 0:
                    LPS.append(0)
                    c += 1
                else:
                    p = LPS[p - 1]

        stack = [('', 0)]
        i, j = 0, 0
        while i < m:
            if s[i] == part[j]:
                j += 1
                stack.append((s[i], j))
                i += 1
            else:
                if j == 0:
                    stack.append((s[i], j))
                    i += 1
                else:
                    j = LPS[j - 1]
            if j == n:
                while j:
                    stack.pop()
                    j -= 1
                j = stack[-1][1]

        return ''.join(map(lambda x: x[0], stack))
