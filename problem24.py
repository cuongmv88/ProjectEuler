import math
from itertools import permutations


def sum_of_n_factorial(n):
    result = 0
    for i in range(1,n+1):
        result += math.factorial(i)
    return result


# return length of string which has k_th factorial
def length_of_permuataion_string(k):
    index = 1
    while True:
        len = sum_of_n_factorial(index)
        if len < k <= (len + math.factorial(index + 1)):
            return index+1
        index += 1
    return 0

def convertTuple(tup):
    str =  ''.join(tup)
    return str

k = length_of_permuataion_string(1000000)

l = ['0','1','2','3','4','5','6','7','8','9']
if k <= len(l):
    subL = l[len(l)-k:len(l)]

perm = permutations(subL)

perm_k_th = 1000000

ot = list(perm)[perm_k_th-1]

print(convertTuple(ot))