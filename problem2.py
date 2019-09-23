def fib():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


def even(sequence):
    for number in sequence:
        if not number % 2:
            yield number


def under_four_million(sequence):
    for number in sequence:
        if number > 4000000:
            break
        yield number


print(sum(even(under_four_million(fib()))))
