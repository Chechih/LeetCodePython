class Solution:
    symbols = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    symbolsKey = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV', 'M', 'D', 'C', 'L', 'X', 'V', 'I']
    def romanToInt(self, s: str) -> int:
        symbols = self.symbols
        symbolsKey = self.symbolsKey
        rlt = 0
        for sk in symbolsKey:
            count = s.count(sk)
            if(count > 0):
                for i in range(0, count):
                    rlt += symbols[sk]
                s = s.replace(sk, '')
        return rlt

tttt = Solution()
print(tttt.romanToInt("MCMXCIV"))