# json is used in  web app and useful for both frontend and backend
import json
person ={"name":"John","age":22,"city":"New York", "hasChildren":False, "titles":["engineer","programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)
with open("person.json","w") as f:
     json.dump(person, f, indent=4, sort_keys=True)
# check if the given dictionary can be writeen in the json format to accept
# encode custom object using class
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
user = User("John",22)
def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name, 'age':o.age, o.__class__.__name__: True }
    else:
        raise TypeError('Object must be of type User is not JSON serializable')


userJSON= json.dumps(user, default=encode_user)
print(userJSON)
