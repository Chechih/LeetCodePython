class Solution(object):
    def validateStackSequences(self, pushed, popped):
        aRlt = [];
        bRlt = True;
        iCount = len(pushed);

        if(iCount != len(popped)):
            bRlt = False;

        for i in range(0, iCount):
            iTemp = popped[i];
            if(iTemp in pushed):
                iInd = pushed.index(iTemp);
                target = pushed[:(iInd+1)];
                aRlt.extend(target);
                pushed = pushed[(iInd+1):]
            iPop = aRlt.pop();
            if(iPop != iTemp):
                bRlt = False;
                break;
        return bRlt;