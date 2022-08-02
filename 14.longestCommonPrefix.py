from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStr = min(strs, key = len)
        startInd = 0
        strsCount = len(strs)
        minStrCount = len(minStr)
        finded = True
        target = ""
        while(finded and startInd < minStrCount):
            target = minStr[:startInd+1]
            matches = [a for a in strs if a.startswith(target)]
            if(len(matches) != strsCount):
                finded = False
                startInd -=1
                target = minStr[:startInd+1]
            startInd +=1
        return target

tttt = Solution()
print(tttt.longestCommonPrefix(["a"]))