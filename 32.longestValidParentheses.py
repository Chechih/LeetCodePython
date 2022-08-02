from collections import Counter

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stackParenthesesEndInd = {}
        stackParenthesesStartInd = []
        maxLeg = 0
        for i in range(len(s)):
            ss = s[i]
            if(ss == '('):
                stackParenthesesStartInd.append(i)
                stackParenthesesEndInd[i] = None
            else:
                if(len(stackParenthesesStartInd) > 0):
                    finallyLeftParentheses = stackParenthesesStartInd.pop()
                    stackParenthesesEndInd[finallyLeftParentheses] = i
                else:
                    stackParenthesesEndInd[i] = None

        allNowInd = []
        for spk in stackParenthesesEndInd:
            spv = stackParenthesesEndInd[spk]
            if(spv != None):
                allNowInd.append(spk)
                allNowInd.append(spv)
            else:
                if(len(allNowInd) > 0):
                    leg = max(allNowInd) - min(allNowInd) + 1
                    if(maxLeg < leg):
                        maxLeg = leg
                allNowInd = []
        if(len(allNowInd) > 0):
            leg = max(allNowInd) - min(allNowInd) + 1
            if(maxLeg < leg):
                maxLeg = leg
        return maxLeg


tttt = Solution()
print(tttt.longestValidParentheses("(()"))
print(tttt.longestValidParentheses(")()())"))
print(tttt.longestValidParentheses("()(()"))
print(tttt.longestValidParentheses("())()))))"))
print(tttt.longestValidParentheses(")))(()(())(()"))