class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aInt = int(a, 2)#轉成 int
        bInt = int(b, 2)
        add = aInt + bInt
        return "{0:b}".format(add) #轉二禁為字串