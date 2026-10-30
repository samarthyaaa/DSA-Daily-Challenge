# dictionary is datatype which is mutable and unordered
dict={"name":"Max","age":28,"city":"London"}
print(dict)
value= dict["city"]
print(value)
dict["email"]="coolmax@xyz.com" # to assign a new key value pair to the dictionary
print(dict)
# pop() method use to remove the last element
#popitem() used to remove the last inserted element
if "name" in dict:
     print(dict["name"])
# exception handling
try :
     print(dict["name"])
except:
    print("error")
for key, value in dict.items():# to print each key value pair
    print(key,value)
dict_cpy= dict # can also use dict(dict) to copy thr dictionary
print(dict_cpy)
dict_cpy["name"]="Daisy"
print(dict_cpy)
print(dict)
dict1 = {"name":"Max","age":28,"city":"London"}
dict2 = {"name":"Madiline","age":32,"city":"Berlin"}
dict1.update(dict2)
print(dict1)# all the values are updated to dictionary values
# we can use number and tuple as keys but list is not possible
