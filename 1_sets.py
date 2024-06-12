def d():
    print('='*75)
# Python Sets

# What are sets?

# Sets are a collection data type, they are mutable, unordered, unindexible
# All itmes within a set must be unique

#-- Characteristics
# Unordered : Items in sets have no order and therefore cannot be indexed into
# Mutable : You can change how many items a set has, and remove said items
# All elements in a set must be unique, converting a list into a set will remove all duplucate items from the set
# All items inside a set must be immutable

#-- why bother?
# We can esnure the elements are unique
# Instantaneous membership checks
# Straight forward comparison operations

empty_set = set() # we define an empty set with the set() constructor since {} already represent an empty dictionary
print(type(empty_set))

# dictionary data structure- key : value
# Set are structured differently. Sets are just a collection of data, each separated by a comma
new_set = {'one', 'two', 'three'}
print(type(new_set))

d()

# Converting a list into a set to remove duplicate data, then back into a list
alist = ['item', 'item', 'stuff', 'thingy', 'oddity']
set_list = set(alist)
print(set_list)

alist = list(set_list)
print(alist)

d()

# Converting a tuple into a set to eliminate duplicate data, then back into a tuple
atuple = ('item', 'item', 'stuff', 'thingy', 'oddity')
set_tup = set(atuple)
print(set_tup)

atuple = tuple(set_tup)
print(atuple)

d()

# Converting a dictionary into a set, can't convert back into a dictionary though
my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value1'
    }

new_set_values = set(my_dict.values())
print(f"new_set_values: {new_set_values}")

new_set_keys = set(my_dict.keys())
print(f"new_set_keys: {new_set_keys}")

new_set_items = set(my_dict.items())
print(f"new_set_items: {new_set_items}")