import sys

cases, bits = map(int, input().split())

def store(b, i, v, comp, rev):
    if rev:
        i = bits + 1 - i
    if comp:
        v = 1-v
    b[i-1] = v

def query(x):
    print(x)
    sys.stdout.flush()
    return int(input())

for case in range(1, cases + 1):
    same = 0
    diff = 0
    comp = False
    rev = False
    todo = 1
    buff = [0 for i in range(bits)]
    while True:
        left = 10
        comp = False
        rev = False
        if same > 0:
            x = query(same)
            comp = x != buff[same-1]
            left -= 1
        if diff > 0:
            x = query(diff)
            if x != buff[diff-1]:
                rev = not comp
            else:
                rev = comp
            left -= 1
        while left >= 2 and 2*todo <= bits:
            x = query(todo)
            y = query(bits + 1 - todo)
            left -= 2
            store(buff, todo, x, comp, rev)
            store(buff, bits + 1 - todo, y, comp, rev)
            if same == 0 and x == y:
                same = todo
            if diff == 0 and x != y:
                diff = todo
            todo += 1
        if 2*todo > bits:
            # we have everything
            if rev:
                buff.reverse()
            s = ''.join(str(1 - x if comp else x) for x in buff)
            print(s)
            sys.stdout.flush()
            response = input()
            break
        if left == 1:
            query(1) # don't bother tracking these
