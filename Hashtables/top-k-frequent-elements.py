class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = dict()
        bucket = [None] * (len(nums)+1)
        res = []
        for i in range(len(nums)):
            ht[nums[i]] = ht.get(nums[i], 0) + 1
            
        for key in ht:
            if not bucket[ht[key]]:
                bucket[ht[key]] = [key]
            else:
                bucket[ht[key]].append(key)
        
        for i in reversed(range(len(bucket))):
            if bucket[i] is not None:
                for v in bucket[i]:
                    res.append(v)
        return res[:k]
