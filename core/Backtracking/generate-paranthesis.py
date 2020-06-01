class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res,"",0,0,n)
        return res
    
    def backtrack(self,res,s,open_p,close_p,max_len):
        if len(s) == max_len*2:
            res.append(s)
            return res
        if open_p < max_len:
            self.backtrack(res,s+"(",open_p+1,close_p, max_len)
        if close_p < open_p:
            self.backtrack(res,s+")",open_p,close_p+1,max_len)
