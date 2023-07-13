def good_order(x):
    temp = x
    if (temp % 10) % 2 == 0:
        temp //= 10
        while temp > 0:
            if (temp % 10) % 2 == 1:
                return False
            temp //= 10
        return True
    if (temp % 10) % 2 == 1:
        temp //= 10
        while temp > 0:
            if (temp % 10) % 2 == 0:
                return False
            temp //= 10
        return True

print(good_order(1573))