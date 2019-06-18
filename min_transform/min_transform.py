#!/usr/bin/env python
# -*- coding: utf-8 -*-

def F(a, b, tmp={}):
    if not a:
        return len(b)

    if not b:
        return len(a)

    if a == b:
        return 0

    if (a, b) in tmp:
        print("(%s, %s) in tmp" % (a, b))
        return tmp[(a, b)]

    if a[-1] == b[-1]:
        result = F(a[0:-1], b[0:-1], tmp)
        tmp[(a, b)] = result
        return result

    result = min(
            F(a[0:-1], b[0:-1], tmp) + 1,
            F(a[0:-1], b, tmp) + 1,
            F(a, b[0:-1], tmp) + 1
            )
    tmp[(a, b)] = result
    return result


if __name__ == '__main__':    
    print(F('horse', 'ers'))
    #print(F('panckey', 'epan'))
