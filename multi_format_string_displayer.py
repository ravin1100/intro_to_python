# Write a program that displays the same output using all three string formatting methods in Python:

# % formatting
# .format() method
# f-strings

name = "Alice"
age  = 28
city = "Delhi"
print("My name is %s, I am %d years old, and I live in %s." %(name, age, city))

print("My name is {}, I am {} years old, and I live in {}.".format(name, age, city))

print(f"My name is {name}, I am {age} years old, and I live in {city}.")
