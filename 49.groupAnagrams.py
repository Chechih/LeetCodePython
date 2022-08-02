from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = {}
        for s in strs:
            sortS = ''.join(sorted(s))
            if(sortS in strDict):
                strDict[sortS].append(s)
            else:
                strDict[sortS] = [s]
        return strDict.values()

tttt = Solution()
print(tttt.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))