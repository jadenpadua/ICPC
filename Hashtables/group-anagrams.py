class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupedAnagrams = []
        ht = dict()
        for string in strs:
            
            if ''.join(sorted(string)) not in ht:
                ht[''.join(sorted(string))] = []
                       
            ht[''.join(sorted(string))].append(string)
            
        
        for value in ht.values():
            groupedAnagrams.append(value)
            
        return groupedAnagrams
            
