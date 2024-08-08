class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        def getBase(dig3):
            dig3, one = divmod(dig3, 10)
            dig3, ten = divmod(dig3, 10)
            dig3, hun = divmod(dig3, 10)
            res = ''
            if hun:
                res += itos1[hun] + ' Hundred'
            if ten == 1:
                res += itos1[10*ten + one]
            else:
                res += itos10[ten] + itos1[one]
            return res

        itos1 = [
            '', ' One', ' Two', ' Three', ' Four', ' Five', ' Six',
            ' Seven', ' Eight', ' Nine', ' Ten', ' Eleven', ' Twelve',
            ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen',
            ' Seventeen', ' Eighteen', ' Nineteen'
        ]
        itos10 = [
            '', ' Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty',
            ' Sixty', ' Seventy', ' Eighty', ' Ninety'
        ]
        itos1000 = ['', ' Thousand', ' Million', ' Billion', ' Trillion']

        cur, ans = 0, ''
        while num:
            num, dig3 = divmod(num, 1000)
            base = getBase(dig3)
            if base:
                base += itos1000[cur]
            ans = base + ans
            cur += 1

        return ans[1:]
