from functools import reduce


def aggregated_value(f,t):
    if type(t)!=tuple:
        return t
    return reduce(f,[aggregated_value(f,b) for b in t])

print(aggregated_value(sum,(1,2, (3,4), (5,6))))