def xnor(x,y):
    if x is True and y is True:
        return True
    elif x is True and y is False:
        return False
    elif x is False and y is True:
        return False
    elif x is False and y is False:
        return True


print(xnor(2 > 2, 1 == 1))