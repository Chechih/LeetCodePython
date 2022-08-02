from typing import List

class Solution:
    def segmentsWords(self, words: List[str], maxWidth: int) -> List[List[str]]:
        rlt = []
        grouping = []
        groupStrLeg = 0
        for w in words:
            wordLeg = len(w)
            groupStrLeg += wordLeg
            if maxWidth >= groupStrLeg:
                grouping.append(w)
                groupStrLeg +=1 #空白
            else:
                rlt.append(grouping)
                grouping = [w]
                groupStrLeg = wordLeg + 1
        if grouping:
            rlt.append(grouping)
        return rlt
    def addBlankBySegment(self, segmentsWord: List[str], maxWidth: int) -> List[str]:
        rlt = []
        segmentsWordLeg = len(segmentsWord)
        allWords = ''.join(segmentsWord)
        allWordsLeg = len(allWords)
        allSpace = maxWidth - allWordsLeg
        if segmentsWordLeg > 1:
            space = allSpace // (segmentsWordLeg - 1)
            for i in range(segmentsWordLeg - 1):
                thisSpace = space
                sw = segmentsWord[i]
                if space * (segmentsWordLeg - 1) + i + 1 <= allSpace:
                    thisSpace += 1
                rlt.append(sw + ' ' * thisSpace)
        rlt.append(segmentsWord[segmentsWordLeg - 1])
        allWords = ''.join(rlt)
        rlt.append(' ' * (maxWidth - len(allWords)))
        return rlt
    def addBlankByLastSegment(self, segmentsWord: List[str], maxWidth: int) -> str:
        allWords = ' '.join(segmentsWord)
        rlt = allWords + ' ' * (maxWidth - len(allWords))
        return ''.join(rlt)
    def dealWithSegmentsWords(self, segmentsWords: List[List[str]], maxWidth: int) -> List[str]:
        rlt = []
        segmentsWordsLeg = len(segmentsWords)
        for i in range(segmentsWordsLeg -1):
            sw = segmentsWords[i]
            segment = self.addBlankBySegment(sw, maxWidth)
            rlt.append(''.join(segment))
        rlt.append(self.addBlankByLastSegment(segmentsWords[segmentsWordsLeg - 1], maxWidth))
        return rlt
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        segments = self.segmentsWords(words, maxWidth)
        rlt = self.dealWithSegmentsWords(segments, maxWidth)
        return rlt



tttt = Solution()
#print(tttt.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
#print(tttt.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
#print(tttt.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))

print(tttt.fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16))