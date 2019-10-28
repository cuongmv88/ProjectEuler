import time
from mymodule import calculate_time
from mymodule import is_prime, concatenating, findsubsets

#########################################################################3
def prime_pairs(primes):
    pairs = findsubsets(primes, 2)

    for pair in pairs:

        pair0 = concatenating(pair[0], pair[1])
        pair1 = concatenating(pair[1], pair[0]) 
       
        if not is_prime(pair0) or not is_prime(pair1):                

            return False

    return True

def prime_pair(p, q):
    pair0 = concatenating(p, q)
    pair1 = concatenating(q, p) 

    return is_prime(pair0) and is_prime(pair1)


def prime_pair_number_with_list(p, l):
    # l = list(l)
    for e in l:
        if not prime_pair(e, p):
            return False
    return True

def test():

    primes = [3, 5, 13, 17, 19]

    print(prime_pairs(primes))

    # print(is_prime(35))

    return
#########################################################################3

@calculate_time
def main():

    index = 11
    primes = [{3},{5},{7}]

    set_primes = 5

    while True:
        if is_prime(index):
            if {index} not in primes:
                for e in primes:
                    if prime_pair_number_with_list(index, e):
                        temp = {index} | e
                        if len(temp) == set_primes:
                            print(temp)

                            sum60 = 0

                            for e in temp:
                                sum += e
                            
                            print(sum60)

                            return 0
                        primes.append(temp)
            
                primes.append({index})

        index += 2
    
    return 0

if __name__ == "__main__":
    main()

    # test()