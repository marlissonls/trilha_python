# Open function to open the file "MyFile1.txt" 
# (same directory) in read mode and
file1 = open("ex_02.txt", "r")
print(file1.read())
file1.close()
   
# store its reference in the variable file1 
# and "MyFile2.txt" in D:\Text in file2
#file2 = open(r"D:\Text\ex_02.txt", "r+")