class Solution:
    def isNumber(self, s: str) -> bool:
        def valid(num):
            sc = 0
            for n in num:
                if n.isalpha():
                    return 0    # invalid
                elif n == '-':
                    sc += 1

            if sc > 1 or (sc == 1 and num[0] != '-'):
                # more than 1 signs or 1 sign and not in the beginning
                return 0    # invalid

            num = num.split('.')
            dc = len(num)
            if dc == 1:
                # no decimal points
                if (len(num[0]) - sc) > 0:
                    # if there is atleast 1 digit (other than sign char)
                    return 2    # integer
                else:
                    return 0    # invalid
            elif dc > 2:
                # more than 1 decimal points
                return 0    # invalid
            else:
                if valid(num[0]) or valid(num[1]):
                    return 1    # decimal
                else:
                    return 0    # invalid

        s = list(s)
        for i in range(len(s)):
            if s[i] == '+':
                s[i] = '-'
            elif s[i] == 'E':
                s[i] = 'e'
        s = ''.join(s).split('e')

        if len(s) > 2:
            return False
        if len(s) == 1:
            return (valid(s[0]) > 0)
        else:
            return (valid(s[0]) > 0) and (valid(s[1]) == 2)
