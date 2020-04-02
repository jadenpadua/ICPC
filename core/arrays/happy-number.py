class Solution:
    def isHappy(self, n: int) -> bool:
        
            seen = []  
            while n != 1:   
                new_num = 0
                
                while n > 0:
                    new_num += (n % 10) ** 2
                    n = int(n / 10)
                    
                if new_num in seen:
                    return False
                
                else:
                    seen.append(new_num)
                    n = new_num
            return True
