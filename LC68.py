class Solution:
    def helper1(self, l, maxWidth):
        if len(l) == 1:
            return l[0] + " " * (maxWidth - len(l[0]))
        numSpaces = len(l) - 1
        remainingSpace = maxWidth - len("".join(l))
        spaces = remainingSpace // numSpaces
        count = remainingSpace % numSpaces
        res = ""
        for i in range(len(l) - 1):
            res += l[i]
            res += " " * spaces
            if count > 0:
                res += " "
                count -= 1
        res += l[-1]
        return res
    def helper2(self, l, maxWidth):
        if len(l) == 1:
            return l[0] + " " * (maxWidth - len(l[0]))
        res = ""
        numSpaces = len(l) - 1
        sumLenString = len("".join(l))
        for i in range(len(l)-1):
            res += l[i]
            res += " "
        
        res += l[-1]
        res += " "*(maxWidth-numSpaces-sumLenString)
            
        return res
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, dummy = [], []
        curLen = 0
        for word in words:
            if curLen != 0:
                curLen += 1
            curLen += len(word)
            dummy.append(word)
            if curLen > maxWidth:
                dummy.pop()
                res.append(self.helper1(dummy, maxWidth))
                dummy = [word]
                curLen = len(word)
        if dummy != []:
            res.append(self.helper2(dummy, maxWidth))

        return res
