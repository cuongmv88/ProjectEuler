import time
import math
import mymodule


#########################################################################3
def prime_factors(p):
    factors = {}

    index = 2

    temp = p

    while index < p:
        if mymodule.is_prime(temp):
                factors[temp] = 1
                break

        if temp%index == 0:
            if index in factors:
                factors[index] += 1
            else:
                factors[index] = 1
            temp = int(temp/index)
            
            continue

        index += 1

    return factors


#########################################################################3

@mymodule.calculate_time
def main():

    consecutive = 4

    n = 2

    while True:

        index = 0
        for i in range(0, consecutive):
            if len(prime_factors(n + i)) == consecutive:
                index = i
            else:
                break
        
        if index == consecutive - 1:
            print(n)

            break
        else:
            n = n + index + 1 
        
    return 0

if __name__ == "__main__":
    main()