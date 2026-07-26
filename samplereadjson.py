import json

with open("sample.json", "r") as file:
  data = json.load(file)


for d in data:
  print(d["name"])
