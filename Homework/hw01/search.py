t = "GTTTCTAACCTTATTACTACGTAACGAGGTCGTCATGCAATGCTGACCATGCATGCCTGACTCTGACGCTA"
p = "ACGTAACG"

n = len(t)
m = len(p)

total = 0

positions = []

for i in range(n - m + 1):

    new = t[i:i+m]

    j = 0

    while (j < m) and (new[j] == p[j]):

        j += 1

    if j == m:

        total += 1
        positions.append(str(i))

print("Total:", total, "", " ".join(positions))
