class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def dfs(i, tight, nz):
            if i == len(num):
                return nz
            key = (i, tight, nz)
            if key not in memo:
                r = int(num[i]) if tight else 9
                if nz:
                    res = 0
                else:
                    res = dfs(i+1, tight and ('0'==num[i]), False)
                for j in range(len(digits)):
                    if int(digits[j]) > r:
                        break
                    res += dfs(i+1, tight and (digits[j]==num[i]), nz or digits[j]!='0')
                memo[key] = res
            return memo[key]

        memo = {}
        num = str(n)
        return dfs(0, True, False)
