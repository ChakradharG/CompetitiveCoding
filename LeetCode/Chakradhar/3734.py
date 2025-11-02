class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        if len(s) == 1:
            if s > target:
                return s
            else:
                return ''

        arr = [0 for _ in range(26)]
        ch = None
        for k, v in Counter(s).items():
            if v % 2:
                if ch is not None:
                    return ''
                ch = k
            arr[ord(k) - 97] += (v // 2)
        n = len(s) // 2

        def backtrack(i, flag, cur):
            if i == n:
                if ch is not None:
                    cur = cur + ch + cur[::-1]
                else:
                    cur = cur + cur[::-1]
                if cur > target:
                    return cur
                else:
                    return ''
            if flag:
                x = 0
            else:
                x = ord(target[i]) - 97
            for y in range(x, 26):
                if arr[y] == 0:
                    continue
                arr[y] -= 1
                res = backtrack(i+1, flag or y != x, cur + chr(y + 97))
                arr[y] += 1
                if res != '':
                    return res
            return ''

        return backtrack(0, False, '')
