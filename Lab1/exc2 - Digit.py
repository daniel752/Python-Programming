def digit(x):
    ctr = 0
    temp = x
    while temp > 0:
        temp = temp//10
        ctr = ctr + 1
    if ctr == 1:
        print('\033[31m' + 'One digit - ', x, '\033[0m', end=" ")
        if x % 2 == 0:
            print('\033[31m' + 'Even' + '\033[0m')
        else:
            print('\033[31m' + 'Odd' + '\033[0m')
    elif ctr == 2:
        temp = x
        sum_digits = 0
        while temp > 0:
            sum_digits = sum_digits + temp % 10
            temp //= 10
        print('\033[31m' + 'Two digits - ', sum_digits, '\033[0m', end=" ")
        if sum_digits % 2 == 0:
            print('\033[31m' + 'Even' + '\033[0m')
        else:
            print('\033[31m' + 'Odd' + '\033[0m')
    elif ctr == 3:
        temp = x
        sum_digits = 0
        temp_ctr = 1
        while temp > 0:
            if temp_ctr == 1 or temp_ctr == 3:
                sum_digits += temp % 10
            temp //= 10
            temp_ctr += 1
        print('\033[31m' + 'Three digits - ', sum_digits, '\033[0m', end=" ")
        if sum_digits % 2 == 0:
            print('\033[31m' + 'Even' + '\033[0m')
        else:
            print('\033[31m' + 'Odd' + '\033[0m')
    elif ctr == 4:
        temp = x
        sum_digits = 0
        temp_ctr = 1
        while temp > 0:
            if temp_ctr == 2 or temp_ctr == 3:
                sum_digits += temp % 10
            temp //= 10
            temp_ctr += 1
        print('\033[31m' + 'Four digits - ', sum_digits, '\033[0m', end=" ")
        if sum_digits % 2 == 0:
            print('\033[31m' + 'Even' + '\033[0m')
        else:
            print('\033[31m' + 'Odd' + '\033[0m')
    elif ctr == 5:
        temp = x
        sum_digits = 0
        temp_ctr = 1
        while temp > 0:
            if temp_ctr == 3:
                sum_digits += temp % 10
            temp //= 10
            temp_ctr += 1
        print('\033[31m' + 'Four digits - ', sum_digits, '\033[0m', end=" ")
        if sum_digits % 2 == 0:
            print('\033[31m' + 'Even' + '\033[0m')
        else:
            print('\033[31m' + 'Odd' + '\033[0m')
    elif ctr > 5:
        print('\033[31m' + 'Error' + '\033[0m')


digit(164536)

