class Solution:
    symbols = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    symbolsKey = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    def intToRoman(self, num: int) -> str:
        symbols = self.symbols
        symbolsKey = self.symbolsKey
        symbolsKeyCount = len(symbolsKey)
        rlt = ''
        for sk in symbolsKey:
            divide = num // sk
            if(divide != 0):
                for i in range(0, divide):
                    rlt += symbols[sk]
                num %= sk

        return rlt


tttt = Solution()
print(tttt.intToRoman(58))
