def gerador():
    yield 42
    yield 'abacate'
    yield 7
    yield 13
    yield [1, 2, 3]


x = gerador()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
