    def subArraysOfArray(self,arr2):
        arr2 = [1,2,3,4]
        
        for i in range(len(arr2)):
            for j in range(i+1,len(arr2)+1):
                print(arr2[i:j])
