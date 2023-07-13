def count(x, y=0):
    if x == 0:
        return y
    else:
        return count(x // 10, y + 1)


max_dig = temp_dig = 0


def max_digit(x):
    global max_dig, temp_dig
    if x == 0:
        return max_dig
    else:
        temp_dig = x % 10
        if max_dig < temp_dig:
            max_dig = temp_dig
        return max_digit(x // 10)


def weight(x):
    return count(x) + max_digit(x)


print(weight(7145))