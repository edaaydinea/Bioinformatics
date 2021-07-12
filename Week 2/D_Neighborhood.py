chars = "ACGT"

def neighbors(pattern, d):
    assert(d <= len(pattern))

    if d == 0:
        return [pattern]

    r2 = neighbors(pattern[1:], d-1)
    r = [c + r3 for r3 in r2 for c in chars if c != pattern[0]]

    if (d < len(pattern)):
        r2 = neighbors(pattern[1:], d)
        r += [pattern[0] + r3 for r3 in r2]

    print(r)
    return r

def neighbors2(pattern, d):
    print(len( sum([neighbors(pattern, d2) for d2 in range(d + 1)], [])))

neighbors(chars, 3)
neighbors2(chars, 3)