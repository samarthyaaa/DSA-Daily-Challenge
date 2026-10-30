# strings :ordered, immutables, text representation
greeting ="Hello"
name="Tom"
sentence = greeting + " " + name
print(sentence)
for i in greeting:
    print(i)
if 'el' in greeting:
    print('yes')
else:
    print('no')
# .strip()-remove white space
# .upper()-UPPERCASE
#endswith()- if the string endswith this char
# find()- return the index the first occurence of char , else return -1
str = 'how,are,you,doing?'
list1=str.split(",") # return each word as a list element
print(list1)
new_str=' '.join(list1) # to convert the list to str
print(new_str)
# f string
var = 3.123
var2 = 6
str=f'the variable is{var} and {var2}'
print(str)
