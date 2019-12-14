def countPrimes(n):
   
    primes = 0
    for i in range(2,n+1):
        isPrime = True
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime == True: 
            primes += 1
    return primes

print(countPrimes(100))
