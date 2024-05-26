class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(i, cur):
            if i == len(s):
                if cur == '' or cur in wordDict:
                    return [cur]
                else:
                    return [] # can't break

            key = (i, cur)
            if key not in memo:
                memo[key] = dfs(i+1, cur + s[i])
                if cur in wordDict:
                    for sub in dfs(i, ''):
                        memo[key].append(cur + ' ' + sub)
            return memo[key]

        wordDict = set(wordDict)
        memo = {}   # (index, current unbroken string) -> []

        return dfs(0, '')
