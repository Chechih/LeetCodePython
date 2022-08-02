from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numStrs = [str(n) for n in digits]
        num = int(''.join(numStrs))
        num += 1
        numStrs = str(num)
        return [n for n in numStrs]

tttt = Solution()
print(tttt.plusOne([1,2,3]))