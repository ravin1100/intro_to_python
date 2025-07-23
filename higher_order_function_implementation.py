# Implement custom versions of the built-in map(), filter(),
#  and reduce() functions. Use them with lambda expressions to perform 
# data processing tasks like transforming, filtering, and reducing lists.

def custom_map(function, iterable):
    return [function(x) for x in iterable]

print(custom_map(lambda x : x*x, range(5)))

def custom_filter(function, iterable):
    return [x for x in iterable if function(x)]

print(custom_filter(lambda x: x%2==0, range(10)))

def custom_reduce(function, iterable):
    result = iterable[0]
    for x in iterable[1:]:
        result = function(result, x)
    return result

print(custom_reduce(lambda x, y: x+y, range(5)))

# output
# --------
# [0, 1, 4, 9, 16]
# [0, 2, 4, 6, 8]
# 10

