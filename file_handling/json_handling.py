import json

#Python provides a builtin module called json to work with json data

with open("file.json","r") as f:
    data = json.load(f)
    print(data)

    print(data["name"])

#json.dump()-Write python data into a json file
#json.dumps()-Convert python data into a json string
#json.loads()-Convert json strings into python data

student = {"mark" : 90, "location" : "Kochi"}
with open( "file.json","w") as f:
    json.dump(student,f)
