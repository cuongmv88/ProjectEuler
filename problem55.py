import time
from mymodule import calculate_time
from mymodule import is_prime
from mymodule import is_palindrome


#########################################################################3

def reserve_digit(n):
    temp = "".join(str(n)[i] for i in range(len(str(n)) -1, -1, -1))

    return int(temp)

def is_lychrel(n):

    iterations = 50

    temp = n
    
    for i in range(0, iterations):
        temp += reserve_digit(temp)

        if is_palindrome(temp):
            return False

    return True


def test():

    # print(reserve_digit(123))

    print(is_lychrel(4994))

    return 0

#########################################################################3

@calculate_time
def main():
    upper = 10000

    count = 0

    for i in range(1, upper):
        if is_lychrel(i):
            count += 1
    
    print(count)
    
    return 0

if __name__ == "__main__":
    main()

    # test()