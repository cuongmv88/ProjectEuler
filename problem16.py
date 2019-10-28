import math
from mymodule import calculate_time


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

@calculate_time
def main():

    print(sum_digits(2,1000))
    
    return 0

if __name__ == "__main__":
    main()