class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = 0
        for c in s:
            match c:
                case "*":
                    l = max(0, l - 1)
                case "#":
                    l *= 2
                case "%":
                    pass
                case _:
                    l += 1

        if k >= l:
            return "."

        for c in reversed(s):
            match c:
                case "*":
                    l += 1
                case "#":
                    h = l // 2
                    if k >= h:
                        k = h - (l - k)
                    l = h
                case "%":
                    k = l - 1 - k
                case _:
                    l -= 1
                    if k == l:
                        return c
            if k >= l:
                break

        return "."
