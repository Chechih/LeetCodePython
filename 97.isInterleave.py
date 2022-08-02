        #   Ø d b b c a
        # Ø T F F F F F
        # a T F F F F F
        # a T T T T T F
        # b F T T F T F
        # c F F T T T T
        # c F F F T F T

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if sorted(s1 + s2) != sorted(s3):
            return False
        s1Leg = len(s1)
        s2Leg = len(s2)
        dp = [[None for x in range(s2Leg + 1)] for y in range(s1Leg  + 1)] #1是空字串
        dp[0][0] = True
        for i in range(1, s1Leg + 1):#處理 s2 是空字串時
            dp[i][0] = dp[i - 1][0] and s3[i - 1] == s1[i - 1]
        for i in range(1, s2Leg + 1):#處理 s1 是空字串時
            dp[0][i] = dp[0][i - 1] and s3[i - 1] == s2[i - 1]
        for i in range(1, s1Leg + 1):
            for j in range(1, s2Leg + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) \
                    or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1] )
        return dp[-1][-1]



tttt = Solution()
print(tttt.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
# print(tttt.isInterleave(
# "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
# "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
# "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))   