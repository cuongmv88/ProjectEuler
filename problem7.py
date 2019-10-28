import time
from mymodule import calculate_time
from mymodule import is_prime


#########################################################################3
def get_prime(n):
    index = 1

    count = 1  # already count 2 as prime

    if n < 1:
        return None
    if n == 1:
        return 2

    while count < n:
        index += 2
        if is_prime(index):
            count += 1
        
    return index
        
#########################################################################3

@calculate_time
def main():

    try:
        f = open("10000prime.txt", "w")
       
        for i in range(1, 10001):
            f.write(str(get_prime(i)) + "\n")
        
    except Exception as e:
        print("Error:" + str(e))
    finally:
        f.close()

if __name__ == "__main__":
    main()