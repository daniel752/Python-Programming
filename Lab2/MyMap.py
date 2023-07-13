from MyFilter import my_filter


def my_map(lst,func):
    res = []  # empty list for returned elements
    for i in lst:
        res.append(func(i))
    return res


def func1(var):  # func to implement new value in elements of new list (res)
    return var*2


Lst = [1,2,3,4,5,6]
print(my_map(Lst,func1))  # output for my_map func

my_filter_and_map = my_map(my_filter(lambda x: x % 2 == 0,Lst),lambda x: x * 2)
print(my_filter_and_map)  # output my_filter_and_map func
