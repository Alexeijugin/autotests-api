import json

json_data = '''{
"name": "Иван",
"age": 30,
"is_student": false,
"courses": [
    "python",
    "api",
    "QA",
    {
        "name": "Alianc"
    }
],
"adress": {"city": "moscow",
           "zipcode": 32121
           }
}'''

res = json.loads(json_data)

print(res["name"])

data = {"name": "Иван",
        "age": 30,
        "is_student": False}

js = json.dumps(data, indent=4)

print(js)


with open("json_example.json", 'r', encoding="utf-8") as file:
        data = json.load(file)
        print(data, type(data))


with open("json_example.json", 'a', encoding="utf-8") as file:
        json.dump(data, file, indent=3)