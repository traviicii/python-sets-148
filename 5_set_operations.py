from helper import d

# We can merge sets together very 'specifically'

set1 = {-1, 0, 1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5, 6, 7}

#-- set1.union(set2) : return a new set of all items from set1 and set2
# Does not affect the original sets
new_set = set1.union(set2)
print(new_set)

d()

#-- set1.intersection(set2) : return a set of all the items set1 and set2 have in common
intersect = set1.intersection(set2)
print(intersect)

d()

#-- set1.difference(set2) : return a set of all the items from set1 that are different from the items in set2
diff_set = set1.difference(set2)
print(diff_set)

d()

#-- set1.symetric_difference(set2) : return a set of all the items from both sets that don't overlap (not in common)
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)

sym_diff_set.add(10)
print(sym_diff_set)

set1.symmetric_difference_update(set2) # Does the same things as .symetric_difference, however instead of returning a new set, this particular method actually alters/updates the original set the method is applied to
print(set1)