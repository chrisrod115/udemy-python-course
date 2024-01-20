def add(*args):
    tot = 0
    for n in args:
        tot += n
    return tot


print(add(1, 2, 3))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    # print(key)
    # print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(n=2, add=3, multiply=5)
