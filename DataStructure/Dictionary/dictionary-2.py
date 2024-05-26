# Key-value pair

# key: 
# 1. uniqueness, insert duplicate key, old vaule will be overwirtiien by the new key
# 2. immutability: key must be immutable data type include: Strings, Numbers, Tuples

# value:
# value can be any of data type include numbers, string, list, dictionary       


# dictionay with different types of keys and values
ex_dict = {
    'name': 'Alice',            # string key, string value
    42: 'The answer',           # integer key, string value
    3.14:[1, 2, 3],             # float key, list value
    (1, 2): {'x':10, 'y':20},   # tuple key, dictionary value
}

# Accessing values using key
print(ex_dict['name'])
print(ex_dict[42])
print(ex_dict[3.14])
print(ex_dict[(1, 2)])


# invalid key examples

# 1. list as keys
# list are mutable so cannot be used as keys in dictionary
invalid_dict = {
    [1, 2, 3]: 'list as key'   # this will raise a TypeError
}

# 2. dictionary as keys
# dicionary are mutable so cannot be used as keys in dictionary
invalid_dict = {
    {1:'a', 2:'b'}: 'dict as key' # this will raise a TypeError
}


# various data values in dictionary
diverse_dict = {
    'integer':42,
    'float':3.14,
    'string':'hello',
    'list':[1, 2, 3],
    'tuple':(4, 5, 6),
    'nested_dict':{'key':'value'}
}

# accessing values
print(diverse_dict['integer'])
print(diverse_dict['float'])
print(diverse_dict['string'])
print(diverse_dict['list'])
print(diverse_dict['tuple'])
print(diverse_dict['nested_dict'])

# overwriting keys
duplicate_key_dict = {
    'key1': 'value1',
    'key 2': 'value2',
    'key1':'new_value1' # this will overwrite the first key1
}

print(duplicate_key_dict)
