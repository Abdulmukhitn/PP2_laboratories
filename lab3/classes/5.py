import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 31))
primes = list(filter(lambda x: is_prime(x), numbers))
print("Primes from 1 to 30:", primes)
