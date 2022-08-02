from typing import List

class Solution:
    def buildIpAddresses(self, s: str, level: int = 0, res: List[str] = []) -> List[str]:
        if level == 4 :
            if s == '':
                rs = ''.join(res)
                rs = rs[0: -1]
                return [rs]
            else:
                return []
        rlt = []
        for i in range(1, 4):
            if len(s) >= i:
                r = s[: i]
                intR = int(r)
                if intR >= 0 and intR <= 255 and str(intR) == r:
                    res.append(r)
                    res.append('.')
                    rlt += self.buildIpAddresses(s[i:], level + 1, res)
                    res.pop()
                    res.pop()
        return list(set(rlt))
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        return self.buildIpAddresses(s)

tttt = Solution()
print(tttt.restoreIpAddresses("101023"))        