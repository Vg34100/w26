def g(i):
    s = set()
    bit = 0

    while i > 0:
        if i % 2 == 1:
            s.add(bit)
        i = i // 2
        bit = bit + 1

    return s


for i in range(20):
    print(g(i))
