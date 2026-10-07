class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def backtrack(i, cur, depth, rem):
            if i == n:
                if depth == 0:
                    valid.add((cur, rem))
                return
            match s[i]:
                case "(":
                    backtrack(i+1, cur, depth, rem+1)
                    backtrack(i+1, cur+"(", depth+1, rem)
                case ")":
                    backtrack(i+1, cur, depth, rem+1)
                    if depth > 0:
                        backtrack(i+1, cur+")", depth-1, rem)
                case _:
                    backtrack(i+1, cur+s[i], depth, rem)

        n = len(s)
        valid = set()
        backtrack(0, "", 0, 0)

        mn = min([v[1] for v in valid])

        return list(map(lambda x: x[0], filter(lambda v: v[1]==mn, valid)))

