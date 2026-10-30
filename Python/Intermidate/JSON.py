# 1json dumps :dumps convert python dictionary into json string
import json
person={"name":"john","age":30,"city":"new york","haschildren":False,"titles":["engineer","programmer"]}
personjson=json.dumps(person,indent=4,sort_keys=True)
print(personjson)

person_dict=json.loads(personjson)# loads parse json string back into python dictionary
print(person_dict)
# 2. writing and reading json files
with open("person.json","w") as file:# dump write python object directly into file
    json.dump(person,file,indent=4)
with open("person.json","r") as file:
    person_data=json.load(file)
    print(person_data)
# custom class encoding:custom class need custom encoding function to convert to json
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
user_obj=user("max",28)
def encode_user(o):
    if isinstance(o,user):
        return {"name":o.name,"age":o.age,o.__class__.__name__:True}
    else:
        raise TypeError("object is not json serializable")
userjson=json.dumps(user_obj,default=encode_user)
print(userjson)
