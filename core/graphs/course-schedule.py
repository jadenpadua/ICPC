class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = 0
        n = numCourses
        p = prerequisites
        inDegree = [0 for i in range(n)]
        for i in range(len(p)):
            inDegree[p[i][0]] += 1
        
        stack = []
        
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                stack.append(i)
        
        while len(stack) != 0:
            curr = stack.pop()
            count += 1
            
            for i in range(len(p)):
                if p[i][1] == curr:
                    inDegree[p[i][0]] -= 1
                    if inDegree[p[i][0]] == 0:
                        stack.append(p[i][0])
        
        return count == n
                    
            
