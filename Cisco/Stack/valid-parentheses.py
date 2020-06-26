class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ht = {"(":")", "{":"}", "[":"]"}
        opening = "({["
        closing = ")}]"
        
        for i in range(len(s)):
            if len(stack) == 0 and s[i] in closing:
                return False
            if s[i] in opening:
                stack.append(s[i])
                
            else:
                if ht[stack.pop()] != s[i]:
                    return False
        return len(stack) == 0
        
                    
