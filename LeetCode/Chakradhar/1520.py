class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        ls, rs = {}, {}
        for i, c in enumerate(s):
            if c not in ls:
                ls[c] = i
            rs[c] = i

        ans = []
        stack = []
        for i, c in enumerate(s):
            stack.append((i, c))
            if i == rs[c]:
                l = ls[c]
                while stack and stack[-1][0] != l:
                    c2 = stack[-1][1]
                    if rs[c2] > rs[c]:
                        ls[c] = l
                        break
                    l = min(l, ls[c2])
                    stack.pop()
                if stack and stack[-1][0] == l:
                    ans.append(s[l:rs[c]+1])
                    stack = []
                else:
                    stack.append((i, c))

        return ans

