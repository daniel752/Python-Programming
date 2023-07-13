def reduce(x):
    if x == 0:
        return x
    if x % 10 == 0:
        return reduce(x//10)
    temp = x % 10
    return reduce(x//10) * 10 + temp


print(reduce(1001201))
