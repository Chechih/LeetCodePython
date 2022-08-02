# 先載入正規表達式的套件 re (Regular Expressions)
import re

class Solution:
    maxNum = 2147483647
    minNum = -2147483648
    def firstCharIsNumber(self, s: str) -> bool:
        finded1 = re.findall(r'-|\+|\d', s[0])#判斷地一個字元是否是符號或數字
        finded2 = re.findall(r'-?\d', s)
        return len(finded1) > 0 and len(finded2) > 0
    def myAtoi(self, s: str) -> int:
        s = s.strip()#字串左右兩邊空格拿掉
        if(len(s) > 0 and not self.firstCharIsNumber(s[0:2])):
            return 0
        allNum = re.findall(r'-?\d+\.?\d*', s) #用正規表示找出所有數字
        rlt = 0
        if(len(allNum) >0):
            rlt = int(float(allNum[0]))
        if(rlt > self.maxNum):
            return self.maxNum
        elif(rlt < self.minNum):
            return self.minNum
        else:
            return rlt
        
tttt = Solution()
print(tttt.myAtoi("   +0 123"))