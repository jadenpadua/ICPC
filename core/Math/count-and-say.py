class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(n-1):
            res = self.helper(res)
        return res
    
    def helper(self,n):
        count = 1
        i = 0
        res = ""
        while i < len(n) - 1:
            if n[i] == n[i+1]:
                count += 1
            else:
                res += str(count) + n[i]
                count = 1
            i += 1
        res += str(count) + n[i]
        return res
        
