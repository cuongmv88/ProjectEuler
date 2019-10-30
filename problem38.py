import time


def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        returned_value = func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
        return returned_value

    return inner1


def concatenating(m, n):
    return int(str(m) + str(n))


def is_pandigital(n):
    digital_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    n_set = set()

    n = str(n)

    if len(n) != 9:
        return False

    for i in range(0, len(n)):
        n_set |= {n[i]}

    return len(digital_set - n_set) == 0


@calculate_time
def pandigital_multiples():
    max_pan = 0
    for k in range(2, 10000, 1):
        temp = k

        for n in range(2, 7):
            temp = concatenating(temp, k * n)
            if len(str(temp)) > 9:
                continue
            if is_pandigital(temp) and max_pan < temp:
                max_pan = temp
                print(temp)

    return max_pan


print(pandigital_multiples())
