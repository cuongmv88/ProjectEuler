import time
import math
from mymodule import calculate_time
from mymodule import is_prime


#########################################################################3
def digit_sum(n):
    sum_digits = 0

    digits = int(math.log10(math.factorial(n))) + 1

    for i in range(1, digits + 1):
        temp = int((factorial_mode(n, 10**i) - factorial_mode(n, 10**(i-1)))/10**(i-1))

        sum_digits += temp

    return sum_digits


def factorial_mode(n, k):
    modval = 1

    for i in range(2, n + 1):
        modval = (modval * (i%k))%k

    return modval

def test():

    print(digit_sum(10))

    print(factorial_mode(10, 39))

    print(math.factorial(10) % 39)

    return
#########################################################################3

@calculate_time
def main():

    print(digit_sum(100))
    
    return 0

if __name__ == "__main__":
    main()

    # test()