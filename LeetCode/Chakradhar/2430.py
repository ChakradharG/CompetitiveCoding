class Solution:
    def deleteString(self, s: str) -> int:
        def dfs(c, offset):
            if c == len(s):
                return 1

            key = (c, offset)
            if key not in memo:
                branch = 0
                p, LPS = 0, [0]
                while c < len(s):
                    if s[p+offset] == s[c]:
                        LPS.append(p + 1)
                        p, c = p + 1, c + 1
                    else:
                        if p == 0:
                            LPS.append(0)
                            c += 1
                        else:
                            p = LPS[p - 1]

                    halfLen, isOdd = divmod(c-offset, 2)
                    if (not isOdd) and (LPS[-1] == halfLen):
                        branch = max(branch, 1 + dfs(c-halfLen+1, offset+halfLen))

                memo[key] = max(1, branch)
                        # cnt += 1
                        # offset += halfLen
                        # p, c = 0, c - halfLen + 1
                        # LPS = [0]

            return memo[key]

        memo = {}
        return dfs(1, 0)
        # print(memo)
        # return dfs(1, 0)


        # LPS = [0]
        # offset = 0
        # p, c = 0, 1

        # cnt = 1

        # return cnt
# 0 0 0 1 2 3 
#       0 0 0 1 2 3
# a b c a b c a b c
# 0 1 2 3 4 5 6 7 8 9

# 0 1
#   0 1
#     0 0 1 1 2
# a a a b a a b
# 0 1 2 3 4 5 6

# 0 1
#   0 1
#     0 1
#       0 1
# a a a a a
# 0 1 2 3 4