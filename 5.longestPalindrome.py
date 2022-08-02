class Solution:
    findedCharIndex = {}
    findedPalindromicSubstring = {}
    def isPalindromicSubstring(self, s: str) -> str:
        if(s in self.findedPalindromicSubstring):
            return self.findedPalindromicSubstring[s]
        chars = list(s)
        charsCount = len(chars)
        for i in range(0, int(charsCount/ 2)):
            if(chars[i] != chars[charsCount - 1 - i]):# 只要左右有不合的直接跳出
                self.findedPalindromicSubstring[s] = False
                return False
        self.findedPalindromicSubstring[s] = True
        return True

    def findAllCharIndex(self, s: str, target: str) -> str:
        if(not target in self.findedCharIndex):
            self.findedCharIndex[target] = [pos for pos, char in enumerate(s) if char == target]
        return self.findedCharIndex[target]

    def longestPalindrome(self, s: str) -> str:
        self.findedCharIndex = {}
        self.findedPalindromicSubstring = {}
        chars = list(s)
        charsCount = len(chars)
        maxPalindromicSubstring = ''
        for i in range(0, charsCount):
            if(len(maxPalindromicSubstring) >= len(s) - i + 1):#如果最大值
                break
            ic = s[i]
            if(maxPalindromicSubstring == ''):
                maxPalindromicSubstring = ic
            allSameCharInds = self.findAllCharIndex(s, ic)
            reversedAllSameCharInds = list(reversed(allSameCharInds))
            for j in reversedAllSameCharInds: 
                if(len(maxPalindromicSubstring) >= j - i + 1):#如果最大值
                    break   
                rangeStr = s[i: j+ 1]
                isPS = self.isPalindromicSubstring(rangeStr)
                if(isPS and len(rangeStr) > len(maxPalindromicSubstring)):
                    maxPalindromicSubstring = rangeStr
                    break
        return maxPalindromicSubstring

tttt = Solution();
print(tttt.longestPalindrome("aacabdkacaa"))
print(tttt.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"));
print(tttt.longestPalindrome("S"));
print(tttt.longestPalindrome("ccc"));
print(tttt.longestPalindrome("zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"));
print(tttt.longestPalindrome("R"));