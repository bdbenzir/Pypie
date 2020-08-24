cases = int(input())
ccccases = int(input())
for cc in range(1, cases+1):
    t = int(input())
    tasks = []
    for i in range(t):
        tasks.append((i, [int(x) for x in input().split()]))
    tasks.sort(key=lambda r: r[1])
    s = ["C" for i in range(t)]
    j = 0
    c = 0
    ok = True
    for k in tasks:
        if k[1][0] >= j:
            s[k[0]] = "J"
            j = k[1][1]
        elif k[1][0] >= c:
            s[k[0]] = "C"
            c = k[1][1]
        else:
            ok = False
            break
    out = ''.join(s) if ok else "IMPOSSIBLE"
    print("Case #{}: {}".format(cc, out))
