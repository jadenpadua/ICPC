class Solution:
    def countElements(self, arr: List[int]) -> int:
        ht = dict()
        count = 0
        for i in range(len(arr)):
            ht[arr[i]] = ht.get(arr[i],0) + 1
        
        for i in range(len(arr)):
            if ht[arr[i]] > 1 and (arr[i] + 1) in ht:
                count += 1
                continue
            if (arr[i] + 1) in arr:
                count += 1
        return count
        
