class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) < 1:
            return True
        
        balance = 0
        
        for i in range(len(s)):
            if s[i] == ')':
                balance -= 1
            else:
                balance += 1
            # Balance still neg even after converting * and (
            if balance < 0:
                return False
        
        # End of loop balance either > 0 or = 0
        # if already balanced
        if balance == 0:
            return True
        
        # Check other way if there is more left brackets
        balance = 0
        for i in reversed(range(len(s))):
            if s[i] == '(':
                balance -= 1
            
            else:
                balance += 1
                
            if balance < 0:
                return False
        # return true if equal to or greater since we checked those cases breviously
        return True
