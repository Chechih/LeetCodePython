class Solution:
    def multipleStr(self, num: str):
        rlt = 0
        for i in num:
            rlt = rlt* 10 + ord(i) - ord('0')
            #ord 將字符轉 ASCII
        return rlt
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.multipleStr(num1) * self.multipleStr(num2))
        
tttt = Solution()
print(tttt.multiply("123", "456"))