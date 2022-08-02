class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        rlt = -1
        if(needle in haystack):
            rlt  = haystack.index(needle)
        return rlt