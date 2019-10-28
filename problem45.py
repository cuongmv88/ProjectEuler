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

def is_square_number(n):
    sqrt = math.sqrt(n)

    return sqrt - int(sqrt) == 0

def triangle(n):
    return int(n*(n+1)/2)

def is_pentagonal(n):
    delta = 1 + 24*n
    
    if is_square_number(delta) and (math.sqrt(delta) + 1)%6 == 0:
        return True

    return False


def pentagonal(n):
    return int(n*(3*n-1)/2)


def is_hexagonal(n):
    delta = 1 + 8*n

    if is_square_number(delta) and (math.sqrt(delta) + 1)%4 == 0:
        return True

    return False

def hexagonal(n):
    return int(n*(2*n-1))

@calculate_time
def main():
    """ Main program """
    index = 286


    while True:
        temp = triangle(index)

        if is_pentagonal(temp) and is_hexagonal(temp):
            print(temp)
            break

        index += 1


if __name__ == "__main__":
    main()