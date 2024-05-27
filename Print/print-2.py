name = "Alice"
age = 30

# formatting output
# 1. use + operator to concatenate the stirng
print("Hello " + name + " !")
# 2. f-string(formatted string literals)
# embed expression inside string literals using curly braces
print(f"Name: {name}, Age: {age}")

# 2.1 formating numbers to specific digit
value = 123.456789
print(f"Formatted value: {value:.2f}")

# 2.2 using function and methods inside curly braces
import math
radius = 7
print(f"The circumference of a circle with radius {radius} is {2 * math.pi * radius: .2f}")

# 2.3 including curly braces
# to includ curly braces in the output, use double curly braces {{ and }}
value = 10
print(f"The value is {{{value}}}")


# Other string method

# use str.format() method
print("Name: {}, Age: {}".format(name, age))
# use %operator
print("Name: %s, Age: %d" % (name, age))
