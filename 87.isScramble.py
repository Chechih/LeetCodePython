class Solution:
    dp = {}
    def runIsScramble(self, s1: str, s2: str) -> bool:
        dp = self.dp
        if (s1, s2) in dp:
             return dp[(s1, s2)]
        if s1 == s2:
            dp[(s1, s2)] = True
            return True
        strLeg = len(s1)
        if strLeg != len(s2) or sorted(s1) != sorted(s2):
            dp[(s1, s2)] = False
            return False
        for i in range(1, strLeg):
            s1Split1 = s1[: i]
            s1Split2 = s1[i: ]
            s2Split1 = s2[: i]#保持原本位子
            s2Split2 = s2[i: ]    
            if self.runIsScramble(s1Split1, s2Split1) and self.runIsScramble(s1Split2, s2Split2):
                dp[(s1, s2)] = True
                return True
            s2Split1 = s2[strLeg - i:]#相反的位子
            s2Split2 = s2[: strLeg - i] 
            if self.runIsScramble(s1Split1, s2Split1) and self.runIsScramble(s1Split2, s2Split2):
                dp[(s1, s2)] = True
                return True
        dp[(s1, s2)] = False
        return False
        
    def isScramble(self, s1: str, s2: str) -> bool:
        self.dp = {}
        rlt = self.runIsScramble(s1, s2)
        return rlt

tttt = Solution()
#print(tttt.isScramble("great", "rgeat"))
#print(tttt.isScramble("abcdefghijklmnopq", "efghijklmnopqcadb"))
print(tttt.isScramble("eebaacbcbcadaaedceaaacadccd","eadcaacabaddaceacbceaabeccd"))