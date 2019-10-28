import time
import math
from mymodule import calculate_time
from mymodule import is_prime


#########################################################################3

def combinatorics(n, r):
    if r > n:
        return None

    return int(math.factorial(n)/(math.factorial(r)*math.factorial(n - r)))
    
def test():

    print(combinatorics(23,10))

#########################################################################3

@calculate_time
def main():

    upper = 100

    ground_limit = 1000000

    count = 0

    for n in range(23, upper + 1):
        for r in range(0, n):
            if combinatorics(n, r) > ground_limit:
                count += 1
    
    print(count)

    return 0

if __name__ == "__main__":
    main()

    # test()