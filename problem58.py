import time
from mymodule import calculate_time
from mymodule import is_prime


#########################################################################3

# Count the numbers of primes in the diagonal of k size length

def count_spiral_primes(k):
    count = 0

    bottom_right = k*k

    bottom_left = bottom_right - k + 1

    top_left = bottom_left - k + 1

    top_right = top_left - k + 1

    
    return is_prime(bottom_left) + is_prime(top_left) + is_prime(top_right)


def test():

    print(count_spiral_primes(5))

    return
#########################################################################3

@calculate_time
def main():

    index = 3

    count = 0

    diagonal_numbers = 1

    while True:
        diagonal_numbers += 4

        count += count_spiral_primes(index)

        if count/diagonal_numbers < 0.1:
            print(index)

            break
        
        index += 2
    
    return 0

if __name__ == "__main__":
    main()

    # test()