import time
from mymodule import calculate_time
from mymodule import is_prime


#########################################################################3
def is_same_digits(m, n):

    m_set = {str(m)[i] for i in range(0, len(str(m)))}

    n_set = {str(n)[i] for i in range(0, len(str(n)))}

    return len(m_set - n_set) == 0 and len(str(m)) == len(str(n))

def test():

    print(is_same_digits(123,124))
    
    print(is_same_digits(123,312))

    print(is_same_digits(123,1233))


    return 0


#########################################################################3

@calculate_time
def main():

    index = 10

    while True:
        count = 0

        for i in range(2, 7):
            if is_same_digits(index, index*i):
                count +=1
        if count == 5:
            print(index)

            return 0
        
        index += 1
        
    return 0

if __name__ == "__main__":
    main()

    # test()