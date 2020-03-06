def addTwoNumbers(a,b):
    #a will be our XOR result and b will be our carry
    #keep going until we have no carry left
    while (b != 0):
        carry = a & b # Calulates the raw position of the carries without left shif
        a = a ^ b # simulates addition with our XOR operator
        b = carry << 1 # now we left shift oru carry to match correct position

        #now our new a is the simulation of addition with XOR
        #now our new b is our updated carry with the left shift
    
    return a
       

print(addTwoNumbers(5,3))
