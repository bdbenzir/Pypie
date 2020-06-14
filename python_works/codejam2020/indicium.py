cases = int(input())

def mymod(a, n):
    k = a % n
    return k if k != 0 else n

def paired(n, d, a):
    base = [d,a]
    for i in range(1,n+1):
        if i == d or i == a:
            continue
        base.append(i)
    mat = [[base[(i - j) % n] for i in range(n)] for j in range(n)]

    mat[n-3][n-2] = base[n-1]
    mat[n-3][0] = a
    for i in range(1,n-3):
        mat[n-3][i] = base[i+2]
        mat[n-1][n-1] = base[1]
        mat[n-2][n-2] = base[1]
        mat[n-1][n-2] = base[0]
        mat[n-2][n-1] = base[0]
    for i in range(0, n-2):
        low = n-2 + (i%2)
        hi = n-1 - (i%2)
        mat[low][i] = base[i+1] if i > 0 else base[2]
        mat[hi][i] = base[i+3] if i < n-3 else base[n-1]
    return mat

def unpaired(n, d, a, b):
    base = [d,a]
    for i in range(1,n+1):
        if i == d or i == a or i == b:
            continue
        base.append(i)
    base.append(b)
    mat = [[base[(i - j) % n] for i in range(n)] for j in range(n)]
    for i in range(n):
        mat[i][n-2], mat[i][n-1] = mat[i][n-1], mat[i][n-2]
    return mat

for case in range(1, cases + 1):
    n, k = map(int, input().split())
    ok = True
    mat = []
    if k < n or k > n*n or k == n+1 or k == n*n - 1:
        ok = False
    elif k % n == 0:
        diag = k // n
        mat = [[mymod(diag + j - i, n) for j in range(n)] for i in range(n)]
    elif n == 3:
        ok = False
    else:
        # find a partition of form  dd...daa or dd...dab
        for i in range(1, n + 1):
            delta = k - i*(n-2)
            if delta >= 2 and delta < 2*n:
                d = i
                a = delta//2
                b = delta - a
                if a == d or b == d:
                    # a=1,d=1 is either n or n+1, already handled
                    # a=1,b=2,d=2 will be treated as 11...1xy
                    a -= 1
                    # b=n,d=n is either n*n or n*n-1, handled
                    # b=n,a=n-1,d=n-1 has to be n, so continue
                    if b == n:
                        continue
                    b += 1
                break
        if a == b:
            mat = paired(n, d, a)
        else:
            mat = unpaired(n, d, a, b)
    if ok:
        print("Case #{}: POSSIBLE".format(case))
        for r in mat:
            print(' '.join(str(x) for x in r))
    else:
        print("Case #{}: IMPOSSIBLE".format(case))
