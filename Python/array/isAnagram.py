class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = []
        for i in range(len(s)):
            letters.append(s[i])
        
        for i in range(len(t)):
            if t[i] in letters:
                letters.remove(t[i])
            else:
                return False
        return True
