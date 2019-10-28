import time
from itertools import permutations, combinations
from mymodule import calculate_time
from mymodule import is_prime

#########################################################################3
def tuple_to_int(_tuple):
    num = ''
    for e in _tuple:
        num += e
    return int(num)


def number_permutations(n):
    digital_set = [str(n)[i] for i in range(0, len(str(n)))]

    perms = permutations(digital_set)

    result =[]

    for e in list(set(perms)):
        result.append(tuple_to_int(e))

    return result


def findsubsets(s, n):
    return list(combinations(s, n))

def is_arithmetic(s):
    if len(s) < 3:
        return False
    else:
        for i in range(0, len(s) - 2):
            if s[i] - s[i+1] != s[i+1] -s[i+2]:
                return False
        return True

#########################################################################3

@calculate_time
def main():
    blacklist = set()

    for i in range(1001, 9999, 2):
        if is_prime(i):
            
            temp = number_permutations(i)

            p_i = sorted([i for i in temp if is_prime(i) and len(str(i)) == 4])

            if i not in blacklist:
                
                if len(p_i) >= 3:
                    for e in findsubsets(p_i,3):
                        if is_arithmetic(e):
                            print(''.join(str(j) for j in e))

            blacklist |= {i for i in p_i}

    return 0

if __name__ == "__main__":
    main()