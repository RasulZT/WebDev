def prt(n, a):
    if n == 0:
        return
    else:
        print(a,end='')
        prt(n - 1, a)


def foo(s, a):
    if s == 0:
        return
    else:
        prt(s, ' ')
        prt(a, '*')
        print()
        foo(s - 1, a + 2)


foo(5, 10)