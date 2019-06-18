def ed(a, b):
    if not a:
        return len(b or '') or 0

    if not b:
        return len(a or '') or 0

    size1 = len(a)
    size2 = len(b)

    last = 0
    tmp = range(size2 + 1)
    value = None

    for i in range(size1):
        tmp[0] = i + 1
        last = i
        for j in range(size2):
            if a[i] == b[j]:
                value = last
            else:
                value = 1 + min(last, tmp[j], tmp[j + 1])
                # print(last, tmp[j], tmp[j + 1], value)
            last = tmp[j+1]
            tmp[j+1] = value
    return value

if __name__ == '__main__':
    print(ed('horse', 'ers'))
    print(ed('panckey', 'epan'))
