from functools import reduce

sqaures = [i*i for i in range(11)]
print(sqaures)

square = lambda i: i*i
print(square(5))

numbers = [i for i in range(11)]
print(numbers)
squares_from_lambda = map(lambda i: i*i , numbers)
print(list(squares_from_lambda))

even_numbers = filter(lambda x : x%2==0, numbers)
print(list(even_numbers))

odd_numbers = filter(lambda x : x%2!=0, numbers)
print(list(odd_numbers))

sum = reduce(lambda x,y: x+y, numbers)
print(sum)


# output
# ==============
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 25
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [0, 2, 4, 6, 8, 10]
# [1, 3, 5, 7, 9]
# 55