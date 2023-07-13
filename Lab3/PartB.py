from functools import reduce
from operator import add


"""func to return average of courses"""
def avg_grades(courses):
    return tuple(map(lambda course: (course[0],sum(course[1])/len(course[1])),courses))


"""func to return courses after adding factors to desires courses"""
def add_factors(courses,factors):
    return tuple(map(lambda course:
                     (course[0],course[1]) if len(tuple(filter(lambda factor:
                                                               factor[0] == course[0], factors))) == 0 else (course[0], tuple(filter(lambda factor: factor[0]==course[0],factors))[0][1]+course[1]),courses))


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


"""testing part c"""
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