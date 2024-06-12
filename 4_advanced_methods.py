from helper import d

# Advanced Set Methods
# Methods that we use to compare 2 sets of data together

set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5, 6, 7}

#-- set1.issubset(set2) : return True if all items from set1 can be found in set2, else False
print(set1.issubset(set2)) # True
print(set2.issubset(set1)) # False

d()

#-- set1.issperset(set2) : return True if set1 contains all items from set2, else False
print(set1.issuperset(set2)) # False
print(set2.issuperset(set1)) # True

d()

#-- set1.isdisjoint(set2) : return True if there are no common items between the two sets
print(set1.isdisjoint(set2)) # False, both sets contain common items

fruit = {'apple', 'banana', 'pear'}
veg_set = {'carrots', 'potatos', 'broccoli'}

print(fruit.isdisjoint(veg_set)) # True, no common items between the two sets