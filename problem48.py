import time
from mymodule import calculate_time
from mymodule import is_prime


#########################################################################3
def power_mode(a, b, c):  # return a^b mode c
    modval = a%c

    temp = modval

    for i in range(1, b):
        temp = (temp * modval) % c

    return temp


def nth_digit(a,b, n):  #a^b

    return int((power_mode(a, b, 10**(n)) - power_mode(a, b, 10**(n-1)))/10**(n-1))


def test():


    return
#########################################################################3

@calculate_time
def main():

    digit48 = ""

    recall = 0

    for i in range(1,11):
        sdigits = 0
        for j in range(1, 1001):
            dj = nth_digit(j, j, i)

            sdigits += dj
        
        sdigits += recall

        print(sdigits)

        digit48 = str(sdigits % 10) + digit48

        recall = int(sdigits/10)   

    print(digit48)
    return 0

if __name__ == "__main__":
    main()