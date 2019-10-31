def to_sorted_string(n):
    return ''.join(sorted(str(n)))


index = 10

store = dict()

while True:
    max_cube = 5
    count = 0

    cube = index ** 3

    temp = to_sorted_string(cube)

    if temp in store:
        store[temp] |= {cube}

        if len(store[temp]) == max_cube:
            print(min(store[temp]))

            exit()
    else:
        store[temp] = {cube}

    index += 1
