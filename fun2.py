x = [1, 2, 3]


def func(zzx):
    zzx[1] = 42
    x = 'blebleble'


func(x)
print(x)


# def pos(a, b, c):
#     print(a, b, c)
#
#
# values = (1, 3, -6)
# val = {'a': 54, 'c': 55, 'b': 123}
#
# pos(c=1, a=4, b="Tomek")
# pos(*values)
# pos(**val)


def func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

#
# func(1, *(2, 3), f=6, *(4, 5))
# func(*(1, 2), e=5, *(3, 4), f=6)
# func(1, **{'b': 2, 'c': 3}, d=4, **{'e': 5, 'f': 6})
# func(c=3, *(1, 2), **{'d': 4}, e=5, **{'f': 6})


def f1(a, b=34, c=4):
    print(a, b, c)


# f1(b=5, a=6, c=7)


def minimum(*n):
    print(type(n))
    if n:
        mn = n[0]
        for val in n[1:]:
            if val < mn:
                mn = val
        print(mn)


# minimum()
# minimum(4, 6, 2, 43)
# minimum(-5, 66, 3322)


def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)
    print(options)


# connect()
# connect(port=9999, user='admin', pwd='12345')
# connect(port=9999, user='admin', pwd='12345', www='comarch.com')


