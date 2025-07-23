# Create a collection of lambda functions for common tasks such as:

# Mathematical calculations (e.g., square, factorial approximation)
# String manipulations (e.g., reverse, uppercase)
# List operations (e.g., filter evens, sum of list)

from functools import reduce

square = lambda x : x*x
print(square(5))

factorial = lambda n : reduce(lambda x, y: x*y, range(1, n+1)) if n>0 else 1 
print(factorial(5))

# using slicing
reverse = lambda s : s[::-1]
print(reverse("ravin"))

uppercase = lambda s : s.upper()
print(uppercase("ravin"))

# numbers = [i for i in range(11)] 

even = lambda n : list(filter(lambda x: x%2 == 0, range(n)))
print(even(15))

sum = lambda n: reduce(lambda x,y: x+y, range(n))
print(sum(10))


# Output
# ----------------------
# 25
# 120
# nivar
# RAVIN
# [0, 2, 4, 6, 8, 10, 12, 14]
# 45

