import time
from mymodule import calculate_time
from mymodule import is_prime
from itertools import combinations

#########################################################################3
def findsubsets(s, n):
    return list(combinations(s, n))

def test():

    num = '56723'

    slices = [i for i in range (0, len(num) - 1)]

    mask = findsubsets(slices, len(num)-1)

    print(mask)

    for e in mask:
        temp = num

        print("new family:")

        for i in range (0, 10):
            for k in e:
                temp = temp[:k] + str(i) + temp[k+1:]
            print(temp)

#########################################################################3

@calculate_time
def main():

    index = 11

    start_sequence = 0  #store the first of sequences, also result

    num = 8

    while True:
        slices = [i for i in range (0, len(str(index)) - 1)]

        for j in range(1, len(str(index))):
            mask = findsubsets(slices, j)   # get all the ways to replace digits with *

            for e in mask:
                temp = str(index)

                count = 0

                sequences = []

                for i in range (0, 10):
                    for k in e:
                        temp = temp[:k] + str(i) + temp[k+1:]
                    
                    if temp[0] == '0':
                        continue                    # ignore when replace first digit with 0
                    
                    if (is_prime(int(temp))):
                        count += 1
                        sequences.append(temp)

                    if count == num:
                        print("Found: {}, e={}".format(str(index), e))
                        
                        print(sequences)

                        print(sequences[0])
                        return 0

        index += 2

    return 0

if __name__ == "__main__":
    main()

    #test()