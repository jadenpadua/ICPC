class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        left = 0
        right = 0
        uniques = set()
        
        while left < len(s) and right < len(s):
            if s[right] not in uniques:
                uniques.add(s[right])
                print(uniques)
                right += 1
                longest = max(longest, len(uniques))
            
            else:
                uniques.remove(s[left])
                left += 1
                
        return longest
                
