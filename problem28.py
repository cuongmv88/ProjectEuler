import time

def calculate_time(func): 
    def inner1(*args, **kwargs): 
        begin = time.time() 
        returned_value = func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin)
        return returned_value
    return inner1 

# sum of number in diagonals which has k number
def sum_spiral_diagonals(k):
    sum28 = 0

    topright = (2*k -1)**2

    topleft = topright - 2*k + 2

    upperleft = topleft -2*k + 2

    upperright = upperleft -2*k + 2

    sum28 = topright + topleft + upperleft + upperright

    return sum28


@calculate_time
def main():
    """ Main program """
    
    n = int((1001 + 1)/2)

    sum28 = 1

    for i in range (2, n + 1):
        sum28 += sum_spiral_diagonals(i)

    print(sum28)

    return 0

if __name__ == "__main__":
    main()