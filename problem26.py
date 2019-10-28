import math


def num_digit(n):
    return int(math.log10(n)) + 1


def calculate_cycle(p):
    ## (A * B) mod C = (A mod C * B mod C) mod C
    ## A^B mod C = ( (A mod C)^B ) mod C

    index = 1
    while p % 5 == 0:
        p = p / 5
    while p % 2 == 0:
        p = p / 2
    if p == 1:
        return 0

    modval = 10 % p

    temp = modval

    while True:

        if temp == 1:
            return index
        temp = (temp * modval) % p

        index += 1

max_recuring_digit = 0

d_max = 1000

valdict = {0: 0}

d_result = 0

for p in range(2, d_max):

    k = calculate_cycle(p)

    if max_recuring_digit < k:
        max_recuring_digit = k
        d_result = p

print(d_result)
