class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//', '/')
        paths = path.split('/')
        newPaths = []
        for p in paths:
            hasPoint = '.' in p
            pointCount = p.count('.')
            if p and not hasPoint and not pointCount:
                newPaths.append(p)
            elif hasPoint and (pointCount > 2 or len(p) > pointCount):
                newPaths.append(p)
            elif hasPoint and pointCount == 2 and newPaths:
                newPaths.pop()
        rlt = '/'.join(newPaths)
        if rlt and rlt[-1] == '/':#最後面是斜線要拿掉
            rlt = rlt[0:-1]
        if not rlt or rlt[0] != '/':#檢查一開始是不是斜線沒有的話加上去
            rlt = '/' + rlt
        return rlt

tttt = Solution()
print(tttt.simplifyPath("/..hidden"))