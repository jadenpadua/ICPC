class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = []
        self.ht = dict()
        for i in range(len(nums)):
            self.add(nums[i])

    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.ht[self.q[0]] > 1:
            self.q.pop(0)
        
        if len(self.q) == 0:
            return - 1
        
        else:
            return self.q[0]

    def add(self, value: int) -> None:
        if value in self.ht:
            self.ht[value] += 1
        
        else:
            self.ht[value] = 1
            self.q.append(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
