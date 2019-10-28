import time
import math

def calculate_time(func): 
    def inner1(*args, **kwargs): 
        begin = time.time() 
        returned_value = func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin)
        return returned_value
    return inner1 


#########################################################################3
def is_triangle(a, b, c):

    return(a+b>c and b+c>a and a+c>b)

def triangle_from_perimeter(p):
    solutions = []

    for i in range(1, int(p/3)):
        if (p**2 -2*p*i)%(2*p-2*i) == 0:
            a = int((p**2 -2*p*i)/(2*p-2*i))
            c = int(math.sqrt(a**2 + i**2))

            if is_triangle(a, i, c):
                solutions.append({a, i, c})

    return solutions

#########################################################################3

@calculate_time
def main():
    max39 = 0
    index = 0

    for p in range (1, 1001):
        temp = triangle_from_perimeter(p)

        if max39 < len(temp):
            max39 = len(temp)
            index = p

    print(index)

    return 0

if __name__ == "__main__":
    main()