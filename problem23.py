import math
from datetime import datetime


def sum_divisors(n):
    sum_div = 1
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n/i:
                sum_div = sum_div + i
            else:
                sum_div = sum_div + i + n / i
    return sum_div


def is_abudant(n):
    return sum_divisors(n) > n


limit = 28123

set_of_abudants = []

sum_two_abudant = set()

start = datetime.now()

for idx in range(1, limit):
    if is_abudant(idx):
        set_of_abudants.append(idx)
        for e in set_of_abudants:
            if e + idx < limit:
                sum_two_abudant |= {e + idx}

end = datetime.now()

print(limit*(limit-1)/2 - sum(sum_two_abudant))
print("running on {}".format(str(end - start)))