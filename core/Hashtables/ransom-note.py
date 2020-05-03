class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ht = dict()
        for i in range(len(magazine)):
            ht[magazine[i]] = ht.get(magazine[i],0) + 1
            
        for i in range(len(ransomNote)):
            if ransomNote[i] not in ht or ht[ransomNote[i]] == 0:
                return False
            
            ht[ransomNote[i]] -= 1
            
        return True
