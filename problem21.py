import math


def sum_divisors(n):
    sum_div = 1
    if n == 1:
        return 1
    count = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_div = sum_div + i + n / i
            count += 2
    return sum_div


amicables = set()

sum21 = 0

for i in range(2, 1000000):
    if i not in amicables:
        temp = sum_divisors(i)

        if i == sum_divisors(temp) and i != temp:
            sum21 = sum21 + i + temp
            amicables |= {i, temp}
            print("{}-{}".format(i, temp))

print(sum21)
