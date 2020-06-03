class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        scosts = sorted(costs, key = lambda x:x[0]-x[1])
        res = 0
        for i in range(len(costs)):
            if i < len(costs) / 2:
                res += scosts[i][0]
            else:
                res += scosts[i][1]
        return res
