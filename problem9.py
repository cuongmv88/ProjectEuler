import time
import math
from mymodule import calculate_time
from mymodule import is_prime


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


def test():



    return
#########################################################################3

@calculate_time
def main():

    abc = triangle_from_perimeter(1000)

    product = 1

    for e in abc[0]:
        product *= e

    print(triangle_from_perimeter(1000))

    print(product)
    
    return 0

if __name__ == "__main__":
    main()

    test()