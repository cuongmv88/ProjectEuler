import time
from mymodule import calculate_time
from mymodule import is_prime


#########################################################################3
# l is sorted list and s is a number. Return the len of consecutive elements of l which has sum of s
# def find_sum(l, s, n):
#     consecutive = n

#     l=sorted(list(l))

#     if n + 1 > len(l):
#         return consecutive

#     # only sum from max consecutive up to len of l
#     for k in range(n + 1, len(l)):
#         mean = s/k

#         for i in range(0, len(l) - k):

#             if l[i] <= mean < l[i+1]:
#                 break

#         for j in range(i-k + 2, i):
#             if j < 0:
#                 continue

#             elif j + k >= len(l):
#                 break

#             temp = 0
#             for h in range(j, j + k):
#                 temp += l[h]
                
#                 if temp > s:
#                     break

#             if temp == s:
#                 consecutive = k
#                 break     
  
#     return consecutive


def add_list_with_scala(l, n):
    temp = [n+e for e in l]

    temp.append(n)

    return temp

#########################################################################3

@calculate_time
def main():

    upper = 100000

    max_consecutives = 0

    max_consecutives_prime = 0

    count = 1

    sum_primes = [2]

    for i in range(3, upper, 2):
        if is_prime(i):
            count += 1

            for index in range(0, len(sum_primes) - max_consecutives):
                sum_primes[index] += i
                temp = sum_primes[index]

                if temp > upper:
                    continue

                if is_prime(temp) and max_consecutives < count - index:
                    max_consecutives = count - index
                    max_consecutives_prime = temp
                
            sum_primes.append(i)
    
    print("{}-{}".format(max_consecutives_prime, max_consecutives))

    return 0

if __name__ == "__main__":
    main()