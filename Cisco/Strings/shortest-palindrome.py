class Solution:
    def shortestPalindrome(self, s: str) -> str:
        both = s + "#" + s[::-1]
        kmp = [0]
        
        for i in range(1,len(both)):
            j = kmp[i-1]
            while j > 0 and both[j] != both[i]:
                j = kmp[j-1]
            kmp.append(j + (1 if both[j] == both[i] else 0))
        return s[kmp[-1]:][::-1] + s
