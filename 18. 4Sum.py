from typing import List

class Solution:
    def checkDigitsAccord(self, numNumber: object, digits: List[int]) -> bool:
        '''
        檢查所有的數字是不是有在 numNumber 裡面
        '''
        digitsTable = {}
        for d in digits:
            if(d in digitsTable):
                digitsTable[d] +=1
            else:
                digitsTable[d] = 1
        for dt in digitsTable:
            if(digitsTable[dt] > numNumber[dt]):
                return False
        return True

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        numNumber = {}#數字有幾個
        for n in nums:#先找出所有數字出現的次數
            if(n in numNumber):
                numNumber[n] +=1
            else:
                numNumber[n] = 1
        rlt = []
        twoSum = {}
        for iVal in nums:
            for jVal in nums:
                add = iVal + jVal
                if(iVal != jVal or numNumber[iVal] > 1):
                    p = sorted([iVal, jVal])
                    if(add in twoSum):
                        if(not(p in twoSum[add])):
                            twoSum[add].append([iVal, jVal])
                    else:
                        twoSum[add] = [[iVal, jVal]]

        for iVal in nums:
            for jVal in nums:
                add = iVal + jVal
                lack = target - add
                if(lack in twoSum):
                    twoSumlack = twoSum[lack]
                    for tsl in twoSumlack:
                        alldigits = sorted(tsl + [iVal, jVal])
                        if(self.checkDigitsAccord(numNumber, alldigits) and not (alldigits in rlt)):
                            rlt.append(alldigits)
        return rlt
        
tttt = Solution()
print(tttt.fourSum([1,0,-1,0,-2,2], 0))