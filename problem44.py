import time
import math

from mymodule import calculate_time

#########################################################################3
def is_square_number(n):
    sqrt = math.sqrt(n)

    return sqrt - int(sqrt) == 0


def is_pentagonal(n):
    delta = 1 + 24*n
    
    if is_square_number(delta) and (math.sqrt(delta) + 1)%6 == 0:
        return True

    return False


def pentagonal(n):
    return int(n*(3*n-1)/2)


#########################################################################3

@calculate_time
def main():

    n = 2

    while True:
        temp = pentagonal(n)

        mid = int((1+math.sqrt(1+12*temp))/6)

        for i in range(1, mid):
            if is_pentagonal(temp - pentagonal(i)) and is_pentagonal(temp - 2*pentagonal(i)):
                print(temp - 2*pentagonal(i))
                return 0

        n += 1

    return 0

if __name__ == "__main__":
    main()