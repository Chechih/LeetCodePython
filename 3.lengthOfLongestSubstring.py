class Solution:
    def lengthOfLongestSubstring(self, s: str):
        aChar = list(s);
        iCharCount = len(aChar);
        sSpilt = "";
        sMax = "";
        for i in range(0, iCharCount):
            sThisChar = s[i];
            sSpilt = sThisChar;
            if(sMax is "" and sSpilt is not ""):
                sMax = sSpilt;
            for j in range(i + 1, iCharCount):
                sThisChar = s[j];
                if(sThisChar in sSpilt):
                    i = j - 1;
                    break;
                else:
                    sSpilt += sThisChar;
                if(len(sSpilt) > len(sMax)):
                    sMax = sSpilt;
        return len(sMax);

ttt = Solution();
# print(ttt.lengthOfLongestSubstring("pwwkew"));#3
# print(ttt.lengthOfLongestSubstring("abcabcbb"))#3
print(ttt.lengthOfLongestSubstring("hkcpmprxxxqw"))#5