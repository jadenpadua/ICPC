class Solution:
    def isHappy(self, n: int) -> bool:
        ht = dict()
        while n >= 1:
            
            if n not in ht:
                ht[n] = ht.get(n,0) + 1
            else:
                return False
            if n == 1:
                return True
            n_string = str(n)
            squares_list = []
            for i in range(len(n_string)):
                squares_list.append(int(n_string[i])**2)
            squares_list_sum = sum(squares_list)
            n = squares_list_sum
            
            print(squares_list)
