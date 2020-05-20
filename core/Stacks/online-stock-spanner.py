class StockSpanner:
    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        res = 1
        while self.s and self.s[-1][0] <= price:
            res += self.s.pop()[1]
        self.s.append([price,res])
        
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
