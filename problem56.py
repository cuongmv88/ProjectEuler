import time
import math
from mymodule import calculate_time
from mymodule import is_prime
from mymodule import num_digit

#########################################################################3
## A^B mod C = ( (A mod C)^B ) mod C
## (A * B) mod C = (A mod C * B mod C) mod C

def power_mode(a, b, c):  # return a^b mode c
    modval = a%c

    temp = modval

    for i in range(1, b):
        temp = (temp * modval) % c

    return temp

def nth_digit(a,b, n):  #a^b

    return int((power_mode(a, b, 10**(n)) - power_mode(a, b, 10**(n-1)))/10**(n-1))


def sum_digits(a, b):
    digits = int(b*math.log10(a)) + 1

    sdigit = 0

    for i in range(1, digits + 1):
        sdigit += nth_digit(a,b,i)

    return sdigit

def test():
    print(52**2)

    print(nth_digit(52,2,4))

    print(sum_digits(52,2))

    return 

#########################################################################3

@calculate_time
def main():

    max56 = 0

    for a in range(1, 100):
        for b in range(1, 100):
            temp = sum_digits(a, b)

            if max56 < temp:
                max56 = temp
    print(max56)

    return 0

if __name__ == "__main__":
    main()

    # test()


