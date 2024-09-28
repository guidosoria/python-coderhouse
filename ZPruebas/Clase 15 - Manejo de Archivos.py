import json

# data = {}

# data['clients'] = []
# data['locations'] = []

# data['clients'].append({
#     'fist_name' : 'Sigrid',
#     'last_name' : 'Mannok',
#     'age' : 27,
# })

# data['clients'].append({
#     'fist_name' : 'Joe',
#     'last_name' : 'Hinners',
#     'age' : 31,
# })

# data['clients'].append({
#     'fist_name' : 'Theodoric',
#     'last_name' : 'Rivers',
#     'age' : 36,
# })

# with open("./json.txt", "w") as f:
#     json.dump(data, f, indent=1)

with open("/Users/gsoria/Documents/Learning/Python/Python - Coderhouse/json.txt", "w") as file:
    json_a_py = json.load(file)
    
print(json_a_py)