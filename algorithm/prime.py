def _odd_iter():
    n = 3
    while True:
        yield n
        n += 2

def _not_divisible(n):
    return lambda x: x%n > 0

def get_prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for i in get_prime():
    if i <10**3:
        print(i)
    else:
        break