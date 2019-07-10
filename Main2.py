import json
import MySQLdb


# From String to Dictionary
person = '{"name":"Ram","languages":["English","French"]}'
person_dict = json.loads(person)

print(person_dict)
print(json.dumps(person_dict,indent=4,sort_keys=True))

# From File person.json
with open("person.json","r") as fp:
    data = json.load(fp)

print(data)

# Dict to Json

person_dict = {'name':'rama','age':35,'address':"bangalore"}
person_json = json.dumps(person_dict)
print(person_json)

# write json dict to File

person_dict = {'name':'rama','age':35,'address':"hyderabad"}

with open("person_w.json","w") as f:
    json.dump(person_dict,f)


