from functools import reduce

def impares(el):
    res = list(filter((lambda x: x % 2), el))
    print(res)
    res = reduce((lambda x, y: x + y), res)
    print(res)


el = list(range(100))

impares(el)
