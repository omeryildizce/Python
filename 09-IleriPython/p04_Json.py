Person ={
    "name" : "ali",
    "language" : ["python","C#"]

}

result = Person["name"]
print(result)

result = Person["language"]
print(result)

import json
from textwrap import indent
person_string ='{"name" : "ali","language" : ["python","C#"]}'

result = json.loads(person_string)
print(result)

sonuc = result["name"]
print(sonuc)

with open("9-IleriPython//p04_person.json","r+",encoding="utf-8") as f:
    data = json.load(f)
    print(data)
    print(data["name"])





person_dict ={
    "name" : "ali",
    "language" : ["python","C#"]
}
result = json.dumps(person_dict)
print(result)
print(type(result))

with open("9-IleriPython//p04_personSave.json","w",encoding="utf-8") as f:
    json.dump(person_dict, f)

person_dict = json.loads(person_string)
result = json.dumps(person_dict,indent=4,sort_keys=True)
print(person_dict)
print(result)