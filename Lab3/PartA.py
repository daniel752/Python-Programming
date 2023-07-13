"""Part A"""

"""Q.1"""

"""func for creating a rectangle"""
def make_rectangle(x,y,length,width):
    rectangle_stats = (x,y,length,width)
    return rectangle_stats


"""func that returns x coordinate from rectangle"""
def x(rect):
    return rect[0]


"""func that returns y coordinate from rectangle"""
def y(rect):
    return rect[1]


"""func that returns length from rectangle"""
def length(rect):
    return rect[2]


"""func that returns width from rectangle"""
def width(rect):
    return rect[3]


"""func that returns diagonal of rectangle"""
def diagonal(rect):
    return length(rect)**2 + width(rect)**2


"""func to print rectangle"""
def print_rectangle(rect):
    print("Rectangle stats:")
    print("Point: (",end="")
    print(x(rect),end=",")
    print(y(rect),end=")")
    print(";Size: (",end="")
    print(length(rect),end=",")
    print(width(rect),end=")")
    print()


"""func to find center coordinates of rectangle"""
def center(rect):
    x1,x2 = x(rect),x(rect)+length(rect)
    y1,y2 = y(rect),y(rect)+width(rect)
    center_rect = ((x1+x2)/2, (y1+y2)/2)  # creating tuple for pair coordinates (x,y)
    return center_rect


"""func to find distance between two rectangle's center"""
def distance(rect1,rect2):
    D = (x(center(rect2))-x(center(rect1)))**2 + (y(center(rect2))-y(center(rect1)))**2  # formula for distance
    return D


"""func to move the rectangle's position with delta x and delta y parameters"""
def move(rect,delta_x,delta_y):
    new_rect = (x(rect)+delta_x,y(rect)+delta_y,length(rect),width(rect))
    return new_rect


"""func to resize the length and width of rectangle"""
def resize(rect,resize_factor):
    new_rect = (x(rect),y(rect),length(rect)*resize_factor,width(rect)*resize_factor)
    return new_rect


"""func to find average rectangle between to rectangle's"""
def average_rectangle(rect1,rect2):
    avg_rec = ((x(rect1)+x(rect2))/2,(y(rect1)+y(rect2))/2,(length(rect1)+length(rect2))/2,(width(rect1)+width(rect2))/2)
    return avg_rec


"""Testing Q.1"""
r1 = make_rectangle(3,4,10,26)
r1
x(r1)
y(r1)
length(r1)
width(r1)
diagonal(r1)
print_rectangle(r1)
center(r1)
distance(r1,make_rectangle(6,9,5,8))
print_rectangle(move(r1, 2, -3))
print_rectangle(resize(r1, 0.5))
print_rectangle(move(resize(r1, 1.5), -8, 2))
r2 = make_rectangle(6, 9, 5, 8)
print_rectangle(average_rectangle(r1, r2))
print_rectangle(average_rectangle(move(r1, -1, -2), resize(average_rectangle(r2,make_rectangle(6, 9, 5, 8)), 2)))
average_rectangle(move(r1, -1, -2), resize(average_rectangle(r2, make_rectangle(6, 9, 5, 8)),2))


"""Q.2"""

"""func to make a vector with size and list of elements"""
def make_vector(size,list):
    vector_stats = (size,list)
    return vector_stats


"""func to return vector's size"""
def size(vec):
    ctr = 0
    for i in values(vec):
        ctr = ctr + 1
    return ctr


"""func to return vector's values"""
def values(vec):
    return vec[1]


"""func to print vector stats"""
def print_vector(vec):
    print("Size: ",end="")
    print(size(vec),end="")
    print(" ; Values: ",end="")
    print(values(vec))
    print()


"""func to return vector's value based on index"""
def value_at(vec,idx):
    if idx<0 or idx>=size(vec):
        return None
    else:
        return (values(vec))[idx]


"""func to reverse current vector"""
def reverse(vec):
    return make_vector(size(vec),values(vec)[::-1])


"""func to return vector's values in absolute"""
def norm1(vec):
    sum = 0
    for i in values(vec):
        sum += abs(i)
    return sum


def norm2(vec):
    sum = 0
    for i in values(vec):
        sum += i**2
    sum = (sum)**(1/2)
    return sum


"""Inserting new value to vector"""
def insert(vec,new_val):
    return make_vector(size(vec),values(vec)+(new_val,))


"""deleting an element in list by searching with index"""
def delete(vec, rem_val_idx):
    for i in range(size(vec)):
        if i == rem_val_idx:
            return make_vector(size(vec),values(vec)[:i]+values(vec)[i+1:])
    return vec


"""func to sort vector's values in list"""
def sort_vector(vec):
    new_list = list(values(vec))
    for i in range(size(vec)):
        for j in range(i+1,size(vec)):
            #if i+1 == size(vec):
             #   i = 0
            if new_list[i] > new_list[j]:
                temp = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = temp
    return make_vector(size(vec),tuple(new_list))


"""func to add two vectors"""
def add_vector(vec1,vec2):
    new_vec = []
    if size(vec1) <= size(vec2):
        for i in range(size(vec1)):
            new_vec.append(value_at(vec1,i) + value_at(vec2,i))
            if i+1 == size(vec1):
                i += 1
                while i < size(vec2):
                    new_vec.append(value_at(vec2,i))
                    i += 1
        return make_vector(i,tuple(new_vec))
    elif size(vec2) < size(vec1):
        for i in range(size(vec2)):
            new_vec.append(value_at(vec1, i) + value_at(vec2, i))
            if i == size(vec2):
                i += 1
                while i < size(vec1):
                    new_vec.append(value_at(vec1, i))
                    i += 1
        return make_vector(i, tuple(new_vec))


"""func to multiply a vector with specific scalar"""
def mult_scalar(vec,scal):
    new_list = list(values(vec))
    for i in range(size(vec)):
        new_list[i] *= scal
    return make_vector(size(vec),tuple(new_list))


"""Testing Q.2"""
v1 = make_vector(5, (1, 2, 3, 4, 5))
v1
size(v1)
values(v1)
print_vector(v1)
print_vector(reverse(v1))
print_vector(v1)
print(value_at(v1, 3))
print(value_at(v1, 8))
print(norm1(v1))
v2 = reverse(insert(insert(v1,6),7))
print(norm2(v2))
print_vector(insert(v1, 6))
print_vector(v2)
print_vector(delete(v2,3))
v3 = delete(delete(delete(v1,0),3),1)
print_vector(v3)
print_vector(delete(v3, 4))
v3 = delete(delete(v3, 0), 0)
print_vector(v3)
print_vector(delete(v3, 2))
print_vector(sort_vector(v2))
print_vector(mult_scalar(v2,3))
print_vector(add_vector(v1,reverse(v2)))
print_vector(add_vector(reverse(add_vector(v1,reverse(v2))),v2))


"""Part B"""

from functools import reduce
from operator import add


"""Q.1"""
"""func to return average of courses"""
def avg_grades(courses):
    return tuple(map(lambda course: (course[0],sum(course[1])/len(course[1])),courses))


"""Q.2"""
"""func to return courses after adding factors to desires courses"""
def add_factors(courses,factors):
    return tuple(map(lambda course:
                     (course[0],course[1]) if len(tuple(filter(lambda factor:
                                                               factor[0] == course[0], factors))) == 0 else (course[0], tuple(filter(lambda factor: factor[0]==course[0],factors))[0][1]+course[1]),courses))


"""Q.3"""
"""func to return average with calculation of credit points"""
def total_average(courses,credits):
    sum_credits = reduce(lambda x,y: x+y[1],credits,0)
    return reduce(lambda total,course:
                  total+(course[1]*((tuple(filter(lambda credit:
                                                  credit[0]==course[0],credits)))[0][1]/sum_credits)),courses,0)


courses = (('a', [81, 78, 57])), ('b', [95, 98]), ('c', [75, 45]), ('d', [58])
print(avg_grades(courses))
factors = (('c', 15), ('a', 20))
print(add_factors(avg_grades(courses), factors))
credits = (('b', 2.5), ('d', 4), ('c', 3.5), ('a', 5))
print(total_average(avg_grades(courses), credits))


"""Part C"""

"""Q.1"""
"""func to create a dictionary of courses info"""
def make_warehouse(courses, credits, types):

    """func to return course grade with maximum credit score"""
    def max_credits():
        max = 0
        for i in credits:
            if max < credits[i]:
                max = credits[i]
                index = i
        return courses[index]

    """func to return course grade with minimum credit score"""
    def min_credits():
        min = 100
        for i in credits:
            if min > credits[i]:
                min = credits[i]
                index = i
        return courses[index]

    """func to return course with maximum grade by type"""
    def max_course(course_type):
        max_grade = 0
        for key,val in courses.items():
            for i in types[course_type]:
                if key == i and max_grade < val:
                    max_grade = val
        return max_grade

    """func to return course with minimum grade by type"""
    def min_course(course_type):
        min_grade = 100
        for key,val in courses.items():
            for i in types[course_type]:
                if key == i and min_grade > val:
                    min_grade = val
        return min_grade

    """func to return average grades of specific courses type"""
    def avg_course(course_type):
        avg = 0
        for key,val in courses.items():
            for i in types[course_type]:
                if key == i:
                    avg += val
        avg /= len(types[course_type])
        return avg

    """func to add course to dictionary"""
    def add_course(course_name,course_grade,course_type):
        new_course = (course_name,)
        if course_type in types:
            types[course_type] += new_course
            courses[course_name] = course_grade
        return courses

    """returning a function based on the user's input """
    return {'min_credits': min_credits, 'max_credits': max_credits, 'max_course': max_course, 'min_course': min_course,
            'avg_course': avg_course, 'add_course': add_course}


"""testing dictionary"""
courses = (('a', 80), ('b', 95), ('c', 75), ('d', 58))
credits = (('a', 2.5), ('b', 4), ('c', 3.5), ('d', 5))
courses_dict = dict(courses)
credits_dict = dict(credits)
types = {'t1':('a', 'b'), 't2':('c',), 't3':('d',)}
w = make_warehouse(courses_dict, credits_dict, types)
print(w['min_credits']())
print(w['max_credits']())
print(w['min_course']('t1'))
print(w['max_course']('t1'))
print(w['avg_course']('t1'))
w['add_course']( 'e', 90, 't2')
print(w['max_course']('t2'))
print(w['min_course']('t2'))
print(w['avg_course']('t2'))

"""Q.2"""

def make_sequence(sequence):

    """func to return filtered tuple"""
    def Filter(bool_func=0):
        if bool_func == 0:
            return sequence
        else:
            return tuple(filter(bool_func, sequence))

    """func to traverse in sequence using 'next' and 'reverse' commands"""
    def filter_iterator(bool_func):
        if bool_func == 0:
            return sequence
        else:
            iter_seq = tuple(filter(bool_func, sequence))
            index = 0

        """func to return the next iterator in sequence"""
        def next_iter():
            nonlocal index
            res = iter_seq[index]
            index = (index + 1) % len(iter_seq)
            return res

        """func to return previous iterator in sequence"""
        def prev_iter():
            nonlocal index
            res = iter_seq[index-1]
            index = (index - 1) % len(iter_seq)
            return res

        """return next/reverse iterator based on syntax"""
        return {'next': next_iter, 'reverse': prev_iter}

    """func to return the sequence in reverse"""
    def reverse():
        return sequence[::-1]

    """func to combine the current sequence with the new sequence"""
    def extend(seq):
        nonlocal sequence
        sequence += seq

    """returning the func to use based on syntax"""
    return {'filter': Filter, 'filter_iterator': filter_iterator, 'reverse': reverse, 'extend': extend}