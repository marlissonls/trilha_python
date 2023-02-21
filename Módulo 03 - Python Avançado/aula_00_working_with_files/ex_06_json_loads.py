# importing the module
import json
  
# reading the data from the file
with open('ex_06_dictionary.txt') as f:
    data = f.read()

print("Data type before reconstruction : ", type(data))

# reconstructing the data as a dictionary
js = json.loads(data)
  
print("Data type after reconstruction : ", type(js))
print(js)

with open('ex_06_dictionary.json') as f:
    datajson = f.read()
  
print("Data type before reconstruction : ", type(datajson))

# reconstructing the data as a dictionary
jsondata = json.loads(datajson)

print("Data type after reconstruction : ", type(jsondata))
print(jsondata)