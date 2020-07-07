# https://edabit.com/challenge/5ou6SKDtFRZugbpda


def additive_persistence(n):
    n = str(n)
    iterations = 0
    while len(n) > 1:
        product = 0
        for i in n:
            product += int(i)
        n = str(product)
        iterations += 1
    return iterations


def multiplicative_persistence(n):
    n = str(n)
    iterations = 0
    while len(n) > 1:
        product = 1
        for i in n:
            product *= int(i)
        n = str(product)
        iterations += 1
    return iterations
