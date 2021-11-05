import json

with open("weather_data_san_antonio.json") as myfile:
    data = json.load(myfile)

json_formatted_str = json.dumps(data, indent=2)

print(json_formatted_str)
