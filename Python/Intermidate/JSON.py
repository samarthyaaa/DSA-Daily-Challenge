#serialization
import json 
person = {"name": "John", "age": 30, "city": "New York",          "hasChildren": False, "titles": ["engineer", "programmer"]}
person_json = json.dumps(person)    
print(person_json)    
print(json.dumps(person,indent=4))
print(json.dumps(person,indent=4,sort_keys=True))

with open("person json","w") as file:
    json.dump(person,file,indent=4)
#deserialization
person=json.loads(person_json)
print(person)
with open("person_json,"r) as file:
    person=json.load(file)
    print(person)
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User("Max", 27)
def encode_user(o):
    if isinstance(o, User):
        return {
            "name": o.name,
            "age": o.age,
            "__class__": o.__class__.__name__
        }
    else:
        raise TypeError("Object of type User is not JSON serializable")

user_json = json.dumps(user, default=encode_user)
print(user_json)
