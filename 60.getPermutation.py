class Solution:
    def getAllPossibleNums(self, n: int) -> int:
        rlt = 1
        for i in range(1, n + 1):
            rlt *= i
        return rlt
    def getFirstNumAndK(self, n: int, k: int, allNums: int, allPossibleNums: int) -> tuple:
        '''
        給出現在的那個數字, 和要找的新 K 值
        '''
        step = allPossibleNums // n #間隔
        minExceeds = 0
        for i in range(1, n + 1):
            if step * i >= k:
                break
            minExceeds += 1
        return (allNums[minExceeds], k - minExceeds *step)
    def getPermutation(self, n: int, k: int) -> str:
        allNums = list(range(1, n + 1))#建立數列陣列 ex:1,2,3,4,....
        rlt = []
        for i in range(n):
            nn = len(allNums)#每次回圈要找的排列
            allPossibleNums = self.getAllPossibleNums(nn)#算有幾種可能
            (firstNum, k) = self.getFirstNumAndK(nn, k, allNums, allPossibleNums)
            rlt.append(firstNum)
            allNums.remove(firstNum)
        return ''.join(map(str, rlt))

tttt = Solution()
print(tttt.getPermutation(1, 1)) 
