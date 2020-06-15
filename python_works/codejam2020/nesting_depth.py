cases = int(input())
for c in range(1, cases+1):
    base = input()
    digits = [int(x) for x in base]
    d = 0
    s = ""
    for i in digits:
        if i > d:
            s += "("*(i-d)
        elif i < d:
            s += ")"*(d-i)
        s += str(i)
        d = i
    if d > 0:
        s += ")" * d
    print("Case #{}: {}".format(c, s))
