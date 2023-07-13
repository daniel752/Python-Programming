def figure(x):
    mid_gap = 0
    for i in range(1, x+1, 1):
        if i == 1:
            print(" " * (x-(i+1)), i, " " * (x-(i+1)))
        elif 1 < i < x:
            print(" " * (x-(i+1)), i, " " * mid_gap, end="")
            print(i)
            mid_gap += 2
        elif i == x:
            for j in range(x, 0, -1):
                print(j, end="")
            for j in range(2, x+1, 1):
                print(j, end="")


figure(7)