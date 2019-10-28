import math
from datetime import  datetime

maxNumber = 1000000

num = 0;  # store max value which has longest chain
chain_num = 0  # store number of max chain

valdict = {0: 0}

start = datetime.now()

for i in range(1, maxNumber):
    count = 1
    temp = i
    while temp != 1:
        if temp % 2 == 0:
            temp = temp / 2
        else:
            temp = 3 * temp + 1

        if temp in valdict:
            count += valdict[temp]
            if chain_num < count:
                num = i
                chain_num = count

            break;
        else:
            count += 1
    valdict.update({i: count})

end = datetime.now()

print(num)
print("run on: {}".format(str(end-start)))
