# importing the module
import ast
  
# reading the data from the file
with open('ex_06_dictionary.txt') as f:
    data = f.read()
  
print("Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
  
print("Data type after reconstruction : ", type(d))
print(d)

print('\n')

# reading the data from the file
with open('ex_06_dictionary.json') as f:
    datajson = f.read()
  
print("Data type before reconstruction : ", type(datajson))
      
# reconstructing the data as a dictionary
djson = ast.literal_eval(datajson)
  
print("Data type after reconstruction : ", type(djson))
print(djson)