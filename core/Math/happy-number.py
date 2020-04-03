class Solution:
    def isHappy(self, n: int) -> bool:
        
        slow = n
        fast = n
        
        slow = self.digitSquareSum(slow);
        fast = self.digitSquareSum(fast);
        fast = self.digitSquareSum(fast);
        
        while slow != fast:
                slow = self.digitSquareSum(slow);
                fast = self.digitSquareSum(fast);
                fast = self.digitSquareSum(fast);
        
        if slow == 1:
            return True
        return False
            
    def digitSquareSum(self,n):
        new_num = 0
        while n > 0:
            new_num += (n % 10) ** 2
            n = int(n / 10)
        return new_num
