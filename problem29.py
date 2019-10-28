import math

lower = 2
upper = 100

sequences = set()
for a in range(lower, upper + 1):
    for b in range(lower, upper + 1):
        sequences |= {a**b}

print(len(sequences))