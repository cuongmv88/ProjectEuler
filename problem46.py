import time
import math
from mymodule import calculate_time
from mymodule import is_prime
from mymodule import is_square_number


#########################################################################3



#########################################################################3

@calculate_time
def main():

    index = 9
    primes = {2, 3, 5, 7}

    while True:
        if is_prime(index):
            primes |= {index}
        else:
            count =  len(primes)
            for e in primes:
                if (index - e)%2 == 0 and is_square_number((index-e)/2):
                    print("{}={} + 2x{}^2".format(index, e, int(math.sqrt((index -e)/2))))
                    break
                else:
                    count -= 1
            
            if count == 0:
                print("Found: {}".format(index))
                break
            
        index += 2 
  
    return 0

if __name__ == "__main__":
    main()