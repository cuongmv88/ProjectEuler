import time
import math


def calculate_time(func): 
    def inner1(*args, **kwargs): 
        begin = time.time() 
        returned_value = func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin)
        return returned_value
    return inner1 


def concatenating(m, n):
    return int(str(m) + str(n))


def is_pandigital(n):
    digital_set = {'1', '2', '3', '4', '5','6', '7', '8', '9'}

    n_set = set()

    n = str(n)

    if len(n) != 9:
        return False

    for i in range(0, len(n)):
        n_set |= {n[i]}

    return len(digital_set - n_set) == 0


def is_product_pandigital(m, n):
    product = m*n
    
    temp = concatenating(m, n)

    temp = concatenating(temp, product)

    return is_pandigital(temp)


@calculate_time
def pandigital_products():
    product_set = set()
    
    sum32 = 0

    for num in range(1000, 9999):
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0 and is_product_pandigital (i, int(num/i)) and num not in product_set:
                sum32 += num
                product_set |= {num}
                print("{} x {} = {}".format(i, int(num/i), num))

    return sum32

print(pandigital_products())
