import math
import time 


head = (2, 3, 5, 7)
tail = (3, 7)

def calculate_time(func): 
    def inner1(*args, **kwargs): 
        begin = time.time() 
        returned_value = func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin)
        return returned_value
    return inner1 


def num_digit(n):
    return int(math.log10(n)) + 1


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    else:
        for i in range(7, int( math.sqrt(n) ), 2):
            if n % i == 0:
                return False
        else:
            return True


def check_head_tail(n):
    length = num_digit(n)

    first = int(n/(10**(length -1)))
    last = n%10

    if first in head and last in tail:
        return True
    return False


def left_prime_truncatable(n):
    length = num_digit(n)

    for i in range(1, length + 1):
        if not is_prime(int(n%10**i)):
            return False

    return True


def right_prime_truncatable(n):
    length = num_digit(n)

    for i in range(0, length):
        if not is_prime(int(n/10**i)):
            return False
    return True


@calculate_time
def prime_truncatables(n):
    count = 0

    index = 10

    total = 0

    while count < n:
        if check_head_tail(index):

            if left_prime_truncatable(index) and right_prime_truncatable(index):
                count += 1
                total += index
                print(index)
        index += 1
    return total

print(prime_truncatables(11))