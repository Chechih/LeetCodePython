class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        for p in s:
            if(p == '(' or p == '[' or p == '{'):
                parentheses.append(p)
            else:
                if(len(parentheses) > 0):
                    popVal = parentheses.pop()
                else:
                    return False
                if((popVal == '(' and p != ')') or
                 (popVal == '[' and p != ']') or 
                 (popVal == '{' and p != '}')):
                    return False
        if(len(parentheses) != 0):
            return False
        return True

tttt = Solution()
print(tttt.isValid(')()'))