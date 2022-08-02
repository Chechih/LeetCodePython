from typing import List
from numpy import void

class Solution:
    rule = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    def gather(self, nums: List[int], monogram: List[str], layer: int = 0, indivual: int = 0, thisTxt: str = '') -> void:
        if(layer >= len(monogram)):
            nums.append(thisTxt)
            return
        for m in monogram[layer]:
            self.gather(nums, monogram, layer + 1, m, thisTxt + m)
        
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits == ''):
            return []
        rule = self.rule
        monogram = []#轉換成的單字集
        rlt = []
        for sd in digits:
            d = int(sd)
            monogram.append(rule[d])
        self.gather(rlt, monogram)
        return rlt

tttt = Solution()
print(tttt.letterCombinations("234"))
