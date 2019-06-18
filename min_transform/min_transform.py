#!/usr/bin/env python
# -*- coding: utf-8 -*-

def F(a, b):
    if not a:
        return len(b)

    if not b:
        return len(a)

    if a == b:
        return 0

    if a[-1] == b[-1]:
        return F(a[0:-1], b[0:-1])

    return min(
            F(a[0:-1], b[0:-1]) + 1,
            F(a[0:-1], b) + 1,
            F(a, b[0:-1]) + 1
            )


if __name__ == '__main__':    
    print(F('horse', 'ers'))
    print(F('panckey', 'epan'))
