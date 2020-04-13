import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq._heapify_max(heap) 
        print(heap)
        while len(heap) > 1:
            stoneOne = heapq._heappop_max(heap)
            stoneTwo = heapq._heappop_max(heap)

            if stoneOne != stoneTwo:
                heapq.heappush(heap,stoneOne - stoneTwo)
                
            heapq._heapify_max(heap) 
            
        return 0 if len(heap) == 0 else heapq._heappop_max(heap)
