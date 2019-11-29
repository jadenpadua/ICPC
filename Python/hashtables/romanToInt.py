class Solution:
    def romanToInt(self, s: str) -> int:
        ht = dict()
        ht['I'] = 1
        ht['V'] = 5
        ht['X'] = 10
        ht['L'] = 50
        ht['C'] = 100
        ht['D'] = 500
        ht['M'] = 1000
        
        prev_value = 0
        running_total = 0
        for i in range(len(s)-1,-1,-1):
            int_val = ht[s[i]]
            if int_val < prev_value:
                running_total -= int_val
            else:
                running_total += int_val
            prev_value = int_val
        return running_total
