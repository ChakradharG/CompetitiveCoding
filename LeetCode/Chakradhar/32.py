class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxCnt = 0
        cnt, cur = 0, 0
        for c in s:
            if c == '(':
                cur += 1
            else:
                cur -= 1
            if cur < 0:
                cur = 0
                maxCnt = max(maxCnt, cnt)
                cnt = 0
            else:
                cnt += 1
                if cur == 0:
                    maxCnt = max(maxCnt, cnt)
        

        cnt, cur = 0, 0
        for c in reversed(s):
            if c == ')':
                cur += 1
            else:
                cur -= 1
            if cur < 0:
                cur = 0
                maxCnt = max(maxCnt, cnt)
                cnt = 0
            else:
                cnt += 1
                if cur == 0:
                    maxCnt = max(maxCnt, cnt)

        return maxCnt