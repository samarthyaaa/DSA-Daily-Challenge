# shallow copy : one level deep, only references of nested child objects
#deep copy : full independent copy
import copy
org =[[1,2,3,4],[5,6,7,8]]
cpy = copy.deepcopy(org) # change to deepcopy
#cpy=list(org) another method
cpy[0][1]=-10
print(cpy)
print(org)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Company:
    def __init__(self,boss,employee):
        self.boss=boss
        self.employee=employee
p1=Person('Alex',50)
p2=Person('Alex',50)
company =Company(p1,p2)
company_clone=copy.deepcopy(company)
company_clone.boss.age=30
print(company_clone.boss.age)
print(company.boss.age)
p2.age=28
print(p2.age)
print(p1.age)
