# tuple is an ordered list but with different barackets() and Immutable
names = ("Roger", "Syd", "Beau")# Creating a Tuple
#indexing
print(names[-1]) 
print(names.index("Syd"))# index position of a specific item
print(len(names)) #length
print("Roger" in names)# in operator:
#slicing is same just like lists and strings
new_tuple = names[0:2]
print(new_tuple)
other_names = ("Judah", "Quincy")#concatenate tuples
all_names = names + other_names
print(all_names) # 'Roger', 'Syd', 'Beau', 'Judah', 'Quincy'
# Dictionaries Key-Value pairs
dog = {"name": "Roger", "age": 8}# Creating a Dictionary
print(dog["name"]) #Roger
print(dog["age"])  #8
.get() 
print(dog.get("name")) #'Roger'

dog["name"] = "Syd"# Updating  key's value
# Adding a new key-value pair:
dog["favorite_food"] = "Meat"
dog["color"] = "brown"
print(dog) 
.pop()
popped_value = dog.pop("color")
print(popped_value) 
.popitem()
last_item = dog.popitem()
print(last_item) 
# using 'in'
print("name" in dog)  # True 
print("Roger" in dog) # False 
len():
print(len(dog)) #2
del dog["age"]# deleting 
copy():
dog_copy = dog.copy()# copying 
