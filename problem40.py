import time
from mymodule import calculate_time, num_digit

#########################################################################3



def test():



    return
#########################################################################3

@calculate_time
def main():

    count_digits = 0

    di = 0  # power of dn (10^0, 10^1,...,10^6)

    product40 = 1

    index = 1

    while di <= 6:
        priv = count_digits

        count_digits += num_digit(index)

        if priv < 10**di <= count_digits:
            dn = int(str(index)[10**di - priv -1])

            print("di={}, index={}, dn={}".format(di, index, dn))

            product40 *= dn

            di += 1

        
        index += 1
    
    print(product40)

    return 0

if __name__ == "__main__":
    main()

    test()