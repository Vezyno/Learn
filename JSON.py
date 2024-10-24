import json

filename = 'user_settings.txt'
myfile = open(filename, mode='w', encoding='Latin-1')
listok = [12,13,123,123,132,465]
json.dump(listok,myfile)
myfile.close()

# =====================================================

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)
print(json_data)