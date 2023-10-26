# importing the module
import pickle
  
# opening file in write mode (binary)
file = open("ex_08_dictionary.txt", "wb")
  
my_dict = {"Name": "John",
           "Age": 21,
           "Id": 28}

# serializing dictionary 
pickle.dump(my_dict, file)
  
# closing the file
file.close()
  
# reading the data from the file
with open('ex_08_dictionary.txt', 'rb') as handle:
    data = handle.read()
  
print("Data type before reconstruction : ", type(data))
  
# reconstructing the data as dictionary
d = pickle.loads(data)
  
print("Data type after reconstruction : ", type(d))
print(d)