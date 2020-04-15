
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s_list = list(s)
        for i in range(len(shift)):
            if shift[i][0] == 0:
                for j in range(shift[i][1]):
                    s_list.append(s_list.pop(0))
            
            else: 
                for j in range(shift[i][1]):
                    s_list.insert(0,s_list.pop())
                
                
                
        return ''.join(s_list)
            
                        
