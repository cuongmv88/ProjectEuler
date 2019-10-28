import time

def calculate_time(func): 
    def inner1(*args, **kwargs): 
        begin = time.time() 
        returned_value = func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin)
        return returned_value
    return inner1 

#########################################################################3
def is_palindrome(n):
    n = str(n)
    count = 0

    for i in range (0, int(len(n)/2)):
        if n[i] == n[len(n) - 1 - i]:
            count += 1
    
    return count == int(len(n)/2)

def test():
    print(is_palindrome(585))

    print(bin(585)[2:])

    print(is_palindrome(bin(585)))

    print(is_palindrome(123421))


#########################################################################3

@calculate_time
def main():
    
  
    upper = 1000000
    sum36 = 0

    for i in range (0, upper):
        if is_palindrome(i) and is_palindrome(bin(i)[2:]):
            print("{}={}_2".format(i, bin(i)[2:]))
            sum36 += i

    print(sum36)

    return 0

if __name__ == "__main__":
    main()

    # test()