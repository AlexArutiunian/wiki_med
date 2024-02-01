import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data2 = []

for d in data:
    if(d["wiki"] == "" and d["wiki_link"] == ""):
        data2.append(d)



with open("new.json", "w", encoding="utf-8") as fp:
    json.dump(data2, fp, indent=2)
