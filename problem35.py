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

#return rotations of digits of n
def number_rotations(n):
    n = str(n)

    if len(n) == 1:
        return None
    
    rotations = []

    for i in range(0, len(n)):
        n = n[-1] + n[0:len(n) -1]
        rotations.append(n)

    result =  {int(e) for e in rotations}

    return result


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


def test():
    print(number_rotations(12345))


    return

@calculate_time
def main():
    
    upper_limit = 1000000
    
    circular_primes = {2, 3, 5, 7}

    for i in range (11, upper_limit, 2):
        if i in circular_primes:
            continue
        
        if is_prime(i):
            temp = number_rotations(i)
            count = 0
            
            for e in temp:
                if not is_prime(e):
                    break
                count += 1

            if count == len(temp):
                circular_primes |= {i}
                circular_primes |= temp

    print(len(circular_primes))
    
    return 0

if __name__ == "__main__":
    main()