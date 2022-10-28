m = int(input())
n = int(input())

primes = []

def isPrime(num):
    for i in range(2, num):
        if num % i == 0: return False
    return num > 1

for num in range(m, n+1):
    print(num)
    if isPrime(num):
        primes.append(num)

print(primes)

if (len(primes) > 0):
    print(sum(primes))
    print(min(primes))
else:
    print(-1)

    
    