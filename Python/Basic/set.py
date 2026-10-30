# sets like tuple but are not in ordered structure and are immutables
set1 = {"roger", "syd", "roger"}# uses curly braces
set2 = {"roger"}
# printing set1 tells that duplicate roger isremoved
print(set1) 
# 'in'
print("roger" in set1)# element exists in a set
#intersection (&):elements present in both sets
intersect=set1&set2
print(intersect) # 'roger'
#union(|):combines elements from both sets with duplicates removed
mod_union=set1|set2
print(mod_union) #'roger', 'syd'
#difference(-):returns elements in set1 that are not in set2
diff=set1-set2
print(diff) #'syd'

print(set2.issubset(set1))   # prints true (set2 is inside set1)
print(set1.issuperset(set2))  # prints true (set1 contains set2)

print(list(set1))# set into list
