# Errors in Dictionary

# 1. access not existent key
# attemp to access key that does not exist will raise KeyError
my_dict = {
    'name': 'Alice',
    'age':25,
    'city':'New York'
}

try:
    print(my_dict['address']) # this will raise KeyError
except KeyError as e:
    print(f"KeyError : {e}") # KeyError : 'address'

# 2. using invalid types as key
# invalid dictionary with a list as key
try:
    invalid_dict = {
        [1, 2, 3]: 'list as key' # this will raise TypeError
    }
except TypeError as e:
    print(f"TypeError: {e}") # TypeError: unhashable type: 'list'


# 3. modifying dictionary during iteration
# modifying dictionary(e.g., adding or removing keys) while iteration will raise RuetimeError
my_dict = {
    'name': 'Alice',
    'age':25,
    'city':'New York'
}

# modifying the dictionary during iteration
try:
    for key in my_dict:
        if key == 'age':
            del my_dict[key] # this will raise RuntimeError
except RuntimeError as e:
    print(f"RuntimeError: {e}") # RuntimeError: dictionary changed size during iteration


# 4. incorrect usage of dictionary method
# using dictionary method incorrectly, such as calling pop() without providing key
# will raise TypeError
my_dict = {
    'name': 'Alice',
    'age':25,
    'city':'New York'
}

try:
    my_dict.pop() # this will raise TypeError
except TypeError as e:
    print(f"TypeError: {e}") # TypeError: pop expected at least 1 argument, got 0