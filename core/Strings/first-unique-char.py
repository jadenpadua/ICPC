class Solution:
    def firstUniqChar(self, s: str) -> int:
        ht = dict()
        for i in range(len(s)):
            ht[s[i]] = ht.get(s[i],0) + 1
        
        for i in range(len(s)):
            if ht[s[i]] == 1:
                return i
        return -1
