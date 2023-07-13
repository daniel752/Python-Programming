def is_primary(x, y=2):
    if x == 1:
        return True
    if x == y:
        return True
    if x % y == 0:
        return False
    else:
        return is_primary(x, y+1)


print(is_primary(13))