# Dictionary

# - unordered, mutable, indexed, 
# - key-value pair(key must be uniqueness and immutable, such as strings, numbers, tuples)
# - value can be any types

# 1. creating dictionary:

# empty dictionary
my_dict = {}

# Dictionary with initial value
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city':'New York'
}

print(my_dict)

# 2. accessing values:

# accessing values by key
print(my_dict['name'])


# using get method to avoid KeyError if key doesn't exist
print(my_dict.get('age'))
print(my_dict.get('address', 'Not found')) # acces non-existent key using get method
# key address does not exist in the dictionary, get method return the default value 'Not found' 
# instead of raising KeyError


# 3. adding and updating values:

# adding new key-value pair
my_dict['address'] = '123 Main St'
print(my_dict)

# updaing an existing value
my_dict['age'] = 26
print(my_dict)

# 4. removing values:

# using pop() method
age = my_dict.pop('age')
print(age)
print(my_dict)

# using del keyword
del my_dict['address']
print(my_dict)

# using popitem() method to remove the last inserted item
last_item = my_dict.popitem()
print(last_item)
print(my_dict)


# 5. iterating over dictionary:

# iterating over key
for key in my_dict:
    print(key, my_dict[key])

# iterating over value
for value in my_dict.values():
    print(value)

# iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

# 6. dictionary methods