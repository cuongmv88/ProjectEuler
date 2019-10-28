import math


def is_prime(n):
    if n < 1:
        return False
    if n == 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_consecutive_quadratic_primes(a, b):
    n = 0

    while True:
        quadratic_formula = n * n + a * n + b
        if is_prime(quadratic_formula):
            n += 1
        else:
            return n

max_consecutives = 0
a = 0
b = 0
for i in range (-1000, 1000):
    for j in range (-1000, 1000):

        k = count_consecutive_quadratic_primes(i, j)
        if max_consecutives < k:
            max_consecutives = k
            a=i
            b=j
print("a={}, b={} and max consecutive quadratic primes is {}".format(a, b, max_consecutives))
print("result: {}".format(a*b))