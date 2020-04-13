class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
    
        
        while len(stones) > 1:
            sorted_stones = sorted(stones)
            if len(sorted_stones) == 1 or len(sorted_stones) == 0:
                break
            
            x = sorted_stones[len(stones)-2]
            y = sorted_stones[len(stones)-1]
            
            if x == y:
                sorted_stones.remove(x)
                sorted_stones.remove(y)
                
            else:
                sorted_stones.remove(x)
                sorted_stones[len(stones)- 2] = y - x
            print(sorted_stones)
            stones = sorted_stones
            
        return stones[0] if len(stones) == 1 else 0
