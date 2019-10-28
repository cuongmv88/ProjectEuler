import time
from mymodule import calculate_time
from mymodule import is_prime


#########################################################################3



def test():



    return
#########################################################################3

@calculate_time
def main():
    upper = 2000000

    sum10 = 2

    index = 3

    while index < upper:
        if is_prime(index):
            sum10 += index
        
        index += 2
    
    print(sum10)
    
    return 0

if __name__ == "__main__":
    main()

    test()