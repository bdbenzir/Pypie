cases = int(input())
for i in range(1, cases+1):
    size = int(input())
    tr = 0
    badrows = 0
    badcols = 0
    cols = [set() for j in range(size)]
    for j in range(size):
        row = [int(x) for x in input().split()]
        if len(set(row)) < size:
            badrows += 1
        tr += row[j]
        for k in range(size):
            cols[k].add(row[k])
    for j in range(size):
        if len(cols[j]) < size:
            badcols += 1
    print("Case #{}:".format(i), tr, badrows, badcols)
