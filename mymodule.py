import time
import math
from itertools import combinations

def calculate_time(func): 
    def inner1(*args, **kwargs): 
        begin = time.time() 
        returned_value = func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin)
        return returned_value
    return inner1 


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    else:
        for i in range(7, int( math.sqrt(n) ) + 1, 2):
            if n % i == 0:
                return False
        else:
            return True


def is_square_number(n):
    sqrt = math.sqrt(n)

    return sqrt - int(sqrt) == 0

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

def is_pandigital(n):

    n_set = set()

    n = str(n)

    digital_set = {str(i) for i in range(1,len(n) + 1)}

    n_set = {n[i] for i in range(0, len(n))}

    return len(digital_set - n_set) == 0


def number_permutations(n):
    digital_set = [str(i) for i in range(1, n + 1)]

    perms = permutations(digital_set)

    result =[]

    for e in list(perms):
        result.append(tuple_to_int(e))

    return result

def is_palindrome(n):
    n = str(n)
    count = 0

    for i in range (0, int(len(n)/2)):
        if n[i] == n[len(n) - 1 - i]:
            count += 1
    
    return count == int(len(n)/2)

def num_digit(n):
    return int(math.log10(n)) + 1

def concatenating(m, n):
    return int(str(m) + str(n))

def findsubsets(s, n):
    return list(combinations(s, n))