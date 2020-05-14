class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        for i in num:
            while s and s[-1] > i and k:
                s.pop()
                k -= 1
            s.append(i)
        #case of already inc order
        while k > 0:
            s.pop()
            k -= 1
            print(s)
        return "0" if len(s) == 0 else str(int("".join(s)))
            
