import math

# Sieve of Eratosthenes Python Code
def prime_eratosthenes(n):
    dump_list = []
    prime_list = []
    for i in range(2, n + 1):
        if i not in dump_list:
            prime_list.append(i)
            for j in range(i * i, n + 1, i):
                dump_list.append(j)
    return prime_list


# Naive Approach Python Code
def prime_Naive(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


def printPrime(n):
    prime_list = []
    for i in range(2, n + 1):
        if prime_Naive(i):
            prime_list.append(i)
    return prime_list


# Sieve of Atkins Python Code
def prime_Atkins(n):
    prime_list = [2, 3]
    sieve = [False] * (n + 1)
    for x in range(1, int(math.sqrt(n)) + 1):
        for y in range(1, int(math.sqrt(n)) + 1):
            q = 4 * x ** 2 + y ** 2
            if q <= n and (q % 12 == 1 or q % 12 == 5):
                sieve[q] = not sieve[q]
            q = 3 * x ** 2 + y ** 2
            if q <= n and q % 12 == 7:
                sieve[q] = not sieve[q]
            q = 3 * x ** 2 - y ** 2
            if x > y and q <= n and q % 12 == 11:
                sieve[q] = not sieve[q]
    for x in range(5, int(math.sqrt(n))):
        if sieve[x]:
            for y in range(x ** 2, n + 1, x ** 2):
                sieve[y] = False

    for a in range(5, n):
        if sieve[a]:
            prime_list.append(a)
    return prime_list
