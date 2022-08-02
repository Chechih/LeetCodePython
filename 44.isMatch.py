class Solution:
    def merageStar(self, p: str) ->str:
        newP = ''
        isStart = False
        for pp in p:
            if(pp == '*' and isStart):
                continue
            if(pp == '*'):
                isStart = True
            else:
                isStart = False
            newP += pp
        return newP
    rltDict = {}
    def callMatch(self, s: str, p: str) -> bool:
        if((s, p) in self.rltDict):
            return self.rltDict[(s, p)]
        if((len(s) <= 0 and p != '*') or (len(p) <= 0 and len(s) > 0)):
            self.rltDict[(s, p)] = False
        elif(p[0] == '?'):
            self.rltDict[(s, p)] = self.callMatch(s[1:], p[1:])
        elif(p[0] == '*'):
            if(p == '*'):
                self.rltDict[(s, p)] = True
            else:
                self.rltDict[(s, p)] = self.callMatch(s[1:], p) or self.callMatch(s, p[1:])
        elif(s[0] == p[0]):
            self.rltDict[(s, p)] = self.callMatch(s[1:], p[1:])
        else:
            self.rltDict[(s, p)] = False
        return self.rltDict[(s, p)]

    def isMatch(self, s: str, p: str) -> bool:
        self.rltDict = {}
        self.rltDict[('','')] =True
        p = self.merageStar(p)
        rlt =  self.callMatch(s, p)
        ''.endswith
        return rlt

tttt = Solution()
print(tttt.isMatch("adceb","*a*b"))

# tttt = Solution()
# print(tttt.isMatch("abefcdgiescdfimde", "ab*cd?i*de"))

# tttt = Solution()
# print(tttt.isMatch("abcabczzzde", "*abc???de*"))

# tttt = Solution()
# print(tttt.isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
# "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))