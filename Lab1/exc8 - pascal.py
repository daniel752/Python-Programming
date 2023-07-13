m = int(input("Enter first number: "))
n = int(input("Enter sec number: "))


def pascal(x, y):
    if y > x:
        print("Error")
        return -1
    if y == 0 or y == x:
        return 1
    return pascal(x - 1, y - 1) + pascal(x - 1, y)


print("(%d,%d) = (%d)" % (m, n, pascal(m, n)))


