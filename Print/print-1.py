# 1. single print
print("hello world")

# 2. print multiple argument
# seperating them with commas
name = "Alice"
age = 30
print("Name:", name, "Age:", age)

# 3. specify the sep(separator) and end
# print function has 2 optional parameters: sep, end

# sep: specifices the seperator between multiple arguments. The default is a space.
print("Name:", name, "Age:", age, sep = ", ")

# end: specifices what to print at the end of the output. The default is a newline character \n
print("Hello", end=" ")
print("world")

# 4. printing to a file
# print the output to a file by using file parameter
with open('output.txt', 'w') as file: # open a file name output.txt in w write mode, with is used to close the file after the code finish executed
    print("Hello world!!", file=file) # write the output to the file object referred by variable file
