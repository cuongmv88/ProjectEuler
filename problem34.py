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


def num_digit(n):
    return int(math.log10(n)) + 1

def digit_factorial(n):
    sum_digit_power = 0

    for digit in map(int, str(n)):
        sum_digit_power += math.factorial(digit)
    return sum_digit_power

@calculate_time
def main():
    """ Main program """
    sum34 = 0
    for i in range (10, 10**6):
        if i == digit_factorial(i):
            sum34 += i
            print(i)
    
    print(sum34)
    return 0

if __name__ == "__main__":
    main()