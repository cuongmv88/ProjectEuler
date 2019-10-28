import math

FibArray = [0, 1]


def num_digit(n):
    return int(math.log10(n)) + 1

index = 2

while True:
    nextFib = FibArray[index - 1] + FibArray[index - 2]
    if (num_digit(nextFib) >= 1000):
        print(index)
        break
    FibArray.append(nextFib)
    index += 1