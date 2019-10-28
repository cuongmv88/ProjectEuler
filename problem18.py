filepath = 'p067_triangle.txt'
c_last = [None] * 15
with open(filepath) as fp:
    line = fp.readline().strip()

    c_last[0] = int(line)

    while line:
        line = fp.readline().strip()

        c = str(line).split(" ")
        row = len(c)

        if row == 1:
            break

        temp = [None] * row  # store sum of previous line with current one

        # calculate first and last items
        temp[0] = int(c[0]) + c_last[0]

        temp[row - 1] = int(c[row - 1]) + c_last[row - 2]

        # for second item it must be compared with two previous
        if row > 2:
            for i in range(1, row - 1):
                temp[i] = max(int(c[i]) + c_last[i - 1], int(c[i]) + c_last[i])
        c_last = temp[:]

print(max(c_last))
