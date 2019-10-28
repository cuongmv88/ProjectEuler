import time
import math
from itertools import permutations

def calculate_time(func): 
    def inner1(*args, **kwargs): 
        begin = time.time() 
        returned_value = func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin)
        return returned_value
    return inner1 

def tuple_to_int(_tuple):
    num = ''
    for e in _tuple:
        num += e
    return int(num)

def number_permutations(n):
    digital_set = [str(i) for i in range(1, n + 1)]

    perms = permutations(digital_set)

    result =[]

    for e in list(perms):
        result.append(tuple_to_int(e))

    return result


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


@calculate_time
def main():
    
    max41 = 0
    index = 9
    while True:
        temp = number_permutations(index)

        for e in temp:
            if e%2 == 0:
                continue

            if is_prime(e) and max41 < e:
                max41 = e
        if max41 > 0:
            break
        index -= 1

    print(max41)
    return 0

if __name__ == "__main__":
    main()