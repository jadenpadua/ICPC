
def main():
    T = int(input())
    for i in range(T):
        caseNumber = i + 1
        matrix = []
        currentMatrix = int(input())
        for i in range(currentMatrix):
            arr = list(map(int, input().split()))
            matrix.append(arr)
        
        k = 0 # Trace of matrix
        r = 0
        for i in range(len(matrix)):
            if len(matrix[i]) != len(set(matrix[i])):
                r += 1 
            for j in range(len(matrix[i])):
                if i == j:
                    k += matrix[i][j]
      
        t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 

        c = 0
        for i in range(len(t_matrix)):
            if len(t_matrix[i]) != len(set(t_matrix[i])):
                c += 1
        
        print("Case #" + str(caseNumber) + ": " + str(k) + " " + str(r) + " " + str(c))
main()
